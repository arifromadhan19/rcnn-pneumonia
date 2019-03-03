import warnings

warnings.filterwarnings('ignore')

import os
import pydicom
import multiprocessing

from PIL import Image
from tqdm import tqdm
from app import application

base_dir = application.config.get('BASE_DIR')
src_path = base_dir + '/app/assets/data/stage_2_train_images'
dst_path = base_dir + '/app/assets/data/stage_2_train_images_png'


def convert(patientId, src_path=src_path, dst_path=dst_path):
    '''
    Convert dcm to png
    '''
    Image.fromarray(
        pydicom.dcmread(
            os.path.join(src_path, patientId + '.dcm')
        ).pixel_array
    ).save(os.path.join(dst_path, patientId + '.png'))


def main():
    assert os.path.lexists(src_path)
    assert os.path.lexists(dst_path)

    patient_ids = [os.path.splitext(f)[0] for f in os.listdir(src_path)]

    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        pbar = tqdm(
            total=len(patient_ids)
            , leave=False
            , desc="Converting"
        )
        for _ in p.imap_unordered(convert, patient_ids):
            pbar.update(1)
        pbar.close()

    print("[Done]!")


if __name__ == '__main__':
    main()
