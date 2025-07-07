#!/bin/bash
#Use ./train_dreamboothlora.script.sh to run (change working directory first)

. /e/MaxSmartWhales/Software/etc/profile.d/conda.sh

conda activate WhaleImageGen

export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"
# export INSTANCE_DIR="C:/Users/hs325/Downloads/25humpbackwhale"
export INSTANCE_DIR="E:/MaxSmartWhales/TrainDreamboothHWIMGs/New"
export OUTPUT_DIR="E:/MaxSmartWhales/ModelsV2/SDXL5e-4GAS2TBS3"
export CUDA_VISIBLE_DEVICES=0

#train_dreambooth_lora.sdxl.py

accelerate launch train_dreambooth_lora_sdxl.py \
  --pretrained_model_name_or_path="$MODEL_NAME" \
  --instance_data_dir="$INSTANCE_DIR" \
  --output_dir="$OUTPUT_DIR" \
  --instance_prompt="a drone image of a humpback whale" \
  --resolution=512 \
  --train_batch_size=3 \
  --gradient_accumulation_steps=2 \
  --learning_rate=5e-4 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps 100 \
  --push_to_hub

#max_train_steps is another unit like epochs