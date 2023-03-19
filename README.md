# GAM : Gradient Attention Module of Optimization for Point Clouds Analysis (AAAI2023)

## Reference
```
@inproceedings{hu2023gam,
  title={GAM : Gradient Attention Module of Optimization for Point Clouds Analysis},
  author={Zhao, Hengshuang and Jiang, Li and Jia, Jiaya and Torr, Philip HS and Koltun, Vladlen},
  author={Hu, Haotian and Wang Fanyi and Su Jingwen and Zhou Hongtao and Wang Yaonong and Hu Laifeng and Zhang Yanhao and Zhang Zhiwang}
  booktitle={Association for the Advance of Artificial Intelligence, AAAI},
  year={2023}
}
```

## Classification (ModelNet40)
### Data Preparation
Download alignment **ModelNet** [here](https://shapenet.cs.stanford.edu/media/modelnet40_normal_resampled.zip) and save in `data/modelnet40_normal_resampled/`.

### Run
You can run different modes with following codes. 
* If you want to use offline processing of data, you can use `--process_data` in the first run. You can download pre-processd data [here](https://drive.google.com/drive/folders/1_fBYbDO3XSdRt3DSbEBe41r5l9YpIGWF?usp=sharing) and save it in `data/modelnet40_normal_resampled/`.

```shell
# ModelNet40
## Select different models in ./models 

## e.g., pointnet2_ssg without normal features
python train_classification.py --model GAM_cls_ssg --log_dir GAM_cls_ssg
python test_classification.py --log_dir GAM_cls_ssg

## e.g., pointnet2_ssg with normal features
python train_classification.py --model GAM_cls_ssg --use_normals --log_dir GAM_cls_ssg_normal
python test_classification.py --use_normals --log_dir GAM_cls_ssg_normal

## e.g., pointnet2_ssg with uniform sampling
python train_classification.py --model GAM_cls_ssg --use_uniform_sample --log_dir GAM_cls_ssg_fps
python test_classification.py --use_uniform_sample --log_dir GAM_cls_ssg_fps
```

### Performance
| Model | Accuracy |
|--|--|
| PointNet2 (Official) | 91.9 |
| PointNet2_SSG (Pytorch without normal) |  92.2|
| PointNet2_SSG (Pytorch with normal) |  92.4|
| GAM_SSG (Pytorch without normal) |  **92.8**|
| PointNet2_MSG (Pytorch with normal) |  92.8|
| GAM_MSG (Pytorch with normal) |  **93.3**|

## Part Segmentation (ShapeNet)
### Data Preparation
Download alignment **ShapeNet** [here](https://shapenet.cs.stanford.edu/media/shapenetcore_partanno_segmentation_benchmark_v0_normal.zip)  and save in `data/shapenetcore_partanno_segmentation_benchmark_v0_normal/`.
### Run
```
## Check model in ./models 
## e.g., pointnet2_msg
python train_partseg.py --model GAM_part_seg_msg --normal --log_dir GAM_part_seg_msg
python test_partseg.py --normal --log_dir GAM_part_seg_msg
```
### Performance
| Model | Inctance avg IoU|
|--|--|
|PointNet2 | 85.1|
|GAM | **85.5**|


## Semantic Segmentation (S3DIS)
### Data Preparation
Download 3D indoor parsing dataset (**S3DIS**) [here](http://buildingparser.stanford.edu/dataset.html)  and save in `data/s3dis/Stanford3dDataset_v1.2_Aligned_Version/`.
```
cd data_utils
python collect_indoor3d_data.py
```
Processed data will save in `data/s3dis/stanford_indoor3d/`.
### Run
```
## Check model in ./models 
## e.g., pointnet2_ssg
python train_semseg.py --model pointnet2_sem_seg --test_area 5 --log_dir pointnet2_sem_seg
python test_semseg.py --log_dir pointnet2_sem_seg --test_area 5 --visual
```
### Performance
|Model  | mIoU | OA | mAcc |
|--|--|--|--|
| PointNet2 | 54.5 | 81.0 | 67.1 |
| GAM | **56.6** | **81.8**| **71.7**|

