import open3d as o3d
import numpy as np


def main(path_data, path_label):
    colors_0 = np.array([[215, 10, 215],
                        [200, 50, 180],
                        [240, 90, 10],
                        [150, 100, 90],
                        [215, 215, 10],
                        [10, 70, 250],
                        [90, 20, 210],
                        [70, 200, 210],
                        [160, 255, 10],
                        [100, 100, 100],
                        [200, 200, 200],
                        [215, 155, 155],
                        [100, 200, 100]]) / 255
    np_pc = np.load(path_data)
    np_true = np_pc[:, 6]
    np_pc = np_pc[:, :3]
    np_label = np.loadtxt(path_label)
    np_label = np_true
    pc_view = o3d.geometry.PointCloud()
    pc_view.points = o3d.utility.Vector3dVector(np_pc)  # 转类型？
    colors = colors_0[np_label.astype(np.uint8)]
    pc_view.colors = o3d.utility.Vector3dVector(colors[:, :3])

    o3d.visualization.draw_geometries([pc_view])  # 可视化


if __name__ == "__main__":
    path_data = 'E:/Pointnet_Pointnet2_pytorch/data/s3dis/stanford_indoor3d/Area_5_office_39.npy'
    path_label = 'E:/Pointnet_Pointnet2_pytorch/log/sem_seg/pointnet2_sem_seg_msg_att/visual/Area_5_office_39.txt'
    path_label = 'E:/Pointnet_Pointnet2_pytorch/log/sem_seg/pointnet2_sem_seg_msg_yuanshi/visual/Area_5_office_39.txt'
    main(path_data, path_label)