#!/usr/bin/env python3

import argparse
import os
import numpy as np
import pydicom
import SimpleITK as sitk

def load_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            return file.read()
    return "README file not found."
        
def load_scan(path):
    reader = sitk.ImageSeriesReader()
    dicom_series = reader.GetGDCMSeriesFileNames(path)
    reader.SetFileNames(dicom_series)
    images = reader.Execute()
    return sitk.GetArrayFromImage(images)

def load_and_extract_segmentation(segmentation_path, segmentation_label):
    segmentation_dicom = pydicom.dcmread(segmentation_path)
    for segment in segmentation_dicom.SegmentSequence:
        if segment.SegmentLabel == segmentation_label:
            return segment
    raise ValueError(f"Segmentation '{segmentation_label}' not found in {segmentation_path}")

def apply_segmentation_and_extract_features(raw_scan_path, segmentation_data):
    raw_scan = load_scan(raw_scan_path)
    segmented_region = raw_scan * segmentation_data  # Placeholder for segmentation application logic
    return extract_features(segmented_region)

def extract_features(segmented_region):
    return np.mean(segmented_region, axis=(1, 2))  # Placeholder for feature extraction logic

def process_patient_data(patient_path):
    patient_features = {}
    for modality in ['ct', 'pet']:
        for segment_label in ['FDG-Avid Tumor', 'Lung']:
            raw_path = os.path.join(patient_path, modality, 'raw')
            segmentation_path = os.path.join(patient_path, modality, 'segmentation')
            segmentation = load_and_extract_segmentation(segmentation_path, segment_label)
            features = apply_segmentation_and_extract_features(raw_path, segmentation)
            patient_features[f'{modality}_{segment_label}_features'] = features
    return patient_features

def process_all_patients(base_path):
    patient_data = {}
    for patient_id in os.listdir(base_path):
        patient_path = os.path.join(base_path, patient_id)
        if os.path.isdir(patient_path):
            patient_data[patient_id] = process_patient_data(patient_path)
    return patient_data

def save_features_as_numpy(patient_data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for patient_id, features in patient_data.items():
        np.save(os.path.join(output_dir, f'{patient_id}_features.npy'), features)

def main(input_dir, output_dir, readme_path):
    all_patient_data = process_all_patients(input_dir)
    save_features_as_numpy(all_patient_data, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=load_readme())
    parser.add_argument('--input', type=str, required=True, help="Input folder containing patient data")
    parser.add_argument('--output', type=str, required=True, help="Output folder for extracted features")
    
    args = parser.parse_args()
    main(args.input, args.output)
