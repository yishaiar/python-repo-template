from app.dotenv import base_dir, data_dir
from app.model.model import  Model
import os

def main():
    print('dotenv params:', {os.getenv('PARAM1')})
    print('base_dir:', base_dir)
    print('data_dir:', data_dir)

    model = Model()
    print('model:', model)

if __name__ == '__main__':
    main()