
#!/bin/bash
# Use: ./train_dreamboothlora_advanced.script.sh (after setting working directory)

. /e/MaxSmartWhales/Software/etc/profile.d/conda.sh
conda activate WhaleImageGen

# Paths and config
export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"
export INSTANCE_DIR="E:/MaxSmartWhales/genAIwhales/TrainDreamboothHWIMGs/New"
export OUTPUT_DIR="E:/MaxSmartWhales/genAIwhales/advancedModels/advancedSDXL2.5e-3"
export CUDA_VISIBLE_DEVICES=0

# Launch training
accelerate launch train_dreambooth_lora_sdxl_advanced.py \
  --pretrained_model_name_or_path="$MODEL_NAME" \
  --instance_data_dir="$INSTANCE_DIR" \
  --output_dir="$OUTPUT_DIR" \
  --instance_prompt="a drone image of a humpback whale in the ocean" \
  --resolution=512 \
  --train_batch_size=2 \
  --gradient_accumulation_steps=1 \
  --learning_rate=2.5e-3 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=100 \
  --rank=4 \
  --push_to_hub
  