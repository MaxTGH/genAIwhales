#!/bin/bash
# Use: ./train_dreamboothlora_advancedv2.script.sh

. /e/MaxSmartWhales/Software/etc/profile.d/conda.sh
conda activate WhaleImageGen

# Config
export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"
export INSTANCE_DIR="E:/MaxSmartWhales/genAIwhales/TrainDreamboothHWIMGs/New"
export OUTPUT_DIR="E:/MaxSmartWhales/genAIwhales/advancedModels/drone-humpback-whale-lora-1"
export CUDA_VISIBLE_DEVICES=0

# Train
accelerate launch train_dreambooth_lora_sdxl_advanced.py \
  --pretrained_model_name_or_path="$MODEL_NAME" \
  --pretrained_vae_model_name_or_path="madebyollin/sdxl-vae-fp16-fix" \
  --instance_data_dir="$INSTANCE_DIR" \
  --output_dir="$OUTPUT_DIR" \
  --instance_prompt="Drone image of a <s0><s1> in the ocean, clear water, visible pectoral fins, ultra realistic" \
  --resolution=1024 \
  --train_batch_size=2 \
  --gradient_accumulation_steps=1 \
  --learning_rate=1.0 \
  --text_encoder_lr=0.5 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=1350 \
  --num_train_epochs=97 \
  --optimizer="prodigy" \
  --prodigy_decouple=True \
  --prodigy_safeguard_warmup=True \
  --prodigy_use_bias_correction=True\
  --rank=16 \
  --mixed_precision="bf16" \
  --gradient_checkpointing \
  --train_text_encoder_ti \
  --train_text_encoder_ti_frac=0.5 \
  --logging_dir="./logs" \
  --report_to="tensorboard" \
  --push_to_hub