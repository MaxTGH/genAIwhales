---
tags:
- text-to-image
- lora
- diffusers
- template:diffusion-lora
- text-to-image
- text-to-image
- diffusers-training
- diffusers
- lora
- template:sd-lora
- stable-diffusion-xl
- stable-diffusion-xl-diffusers
widget:
- text: drone image of a humpback whale
  output:
    url: images/image_5.png
base_model: stabilityai/stable-diffusion-xl-base-1.0
instance_prompt: drone image of a humpback whale
license: openrail++
library_name: diffusers
---
# SDXL LoRA DreamBooth

<Gallery />

## Model description 

These are MaxTGH&#x2F;Model LoRA adaption weights for stabilityai&#x2F;stable-diffusion-xl-base-1.0.

The weights were trained  using [DreamBooth](https:&#x2F;&#x2F;dreambooth.github.io&#x2F;).

LoRA for the text encoder was enabled: False.

Special VAE used for training: None.

Max Train Steps: 200

## Trigger words

You should use `drone image of a humpback whale` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/MaxTGH/SDXLBaseTS200/tree/main) them in the Files & versions tab.
