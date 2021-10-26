# CSRA 

This repo is for the Part 1.

## Environment Configuration

```
docker pull zhouyang996/csra
docker run --name=multi-label --gpus all --shm-size 16G -it --mount type=bind,src=path_to_CSRA_folder,dst=/workspace zhouyang996/csra
```

## Dataset
I've preprocessed the dataset, which can be downloaded from [Google Drive](https://drive.google.com/file/d/1dW0fq9CZ5bcV4ExU1qX5cMI450Y0rGKX/view?usp=sharing).

After downloading it to the root folder, you can decompress using

```
tar -xvf food103.tar
```

THe structure should be like this:

```
|-- data
|   |-- food103
|   |   `-- trainval.json
|   `-- food_public
|       |-- img_dir
|       |   |-- test1
|       |   |   |-- 00004404.jpg
|       |   |   |-- 00004405.jpg
|       |   |   |-- 00004419.jpg
|       |   |   `-- 00007108.jpg
|       |   `-- train
|       |       |-- 00000000.jpg
|       |       |-- 00000001.jpg
|       |       |-- 00000002.jpg
|       |       |-- 00000003.jpg
|       |       |-- 00000004.jpg
```


## Evaluation
You can download the current best-performing models from [Google Drive](https://drive.google.com/file/d/1dg4F1zVW3TT_T49Gi-uY_gPrW-k0MUiR/view?usp=sharing), and put it under: `./checkpoint/vit_B16_224_img_size_224/`.

Then, you can use the following command to test this model on new datasets.

```shell
CUDA_VISIBLE_DEVICES=0 python demo.py --model vit_B16_224 --num_heads 1 --lam 0.3 --dataset food_103 --load_from checkpoint/vit_B16_224_img_size_224/epoch_30.pth --img_dir data/food_public/img_dir/test1 2>&1 | tee vit_B16_224_img_size_224.log
```

You can open the `vit_B16_224_img_size_224.log` file and do some necessary changes (manually) to meet the submission requirements.

### Parameter Tunining
The 82 line in the `demo.py` specify the threshold. TA suggests us to lower the threshold a bit. You may want to see how it affects the performance at Part 1.


## Training

#### Food103
The command for train this model is as follows:

```shell
CUDA_VISIBLE_DEVICES=0 python main.py --model vit_B16_224 --img_size 224 --num_heads 1 --lam 0.3 --dataset food103 --num_cls 103 --save_folder vit_B16_224_img_size_224
```

You may want to try different parameters, e.g. `--num_heads`. 

## Acknowledgement

We thank Lin Sui (http://www.lamda.nju.edu.cn/suil/) for his initial contribution to this project.
