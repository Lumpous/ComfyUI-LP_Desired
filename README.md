# ComfyUI-LP_Desired<br>
Personal ComfyUI-Nodes i just wanted and needed - so why not build them?<br>
A small collection of personal utility nodes built to solve real workflow problems in larger ComfyUI setups.<br>


## Features<br>
- Load Latent (Path)<br>
- Latent Frame Count<br>
- Last Decoded Frame (UI)<br>
- Decoded Frame History (UI)<br>
- WAN Latent Slice<br>
- NHWC -> NCHW (ONNX Fix)<br>
- A1111-compatible image saving<br>

## Requirements<br>
- ComfyUI ≥ 0.6.x<br>
<hr>

## Load Latent (Path)<br>
This node was designed to load previously saved latents<br>
<img src="https://github.com/user-attachments/assets/c579d330-856f-46fb-94ea-1f513ecf572b"><br>
**Inputs:**<br>
- latent_path - STRING<br>

**Outputs:**<br>
- LATENT - LATENT<br>
<hr>  

## Latent Frame Count<br>
Displays the total number of Frames included in input-Latent<br>
<img src="https://github.com/user-attachments/assets/fae82266-1d2a-4e28-bb55-8c71139316b9"><br>
**Inputs:**<br>
- LATENT - LATENT<br>

**Outputs:**<br>
- frame_count - INT<br>
<hr>

## Last Decoded Frame (UI)<br>
Displays the last decoded Frame<br>
<img src="https://github.com/user-attachments/assets/d3d24124-790f-4f4f-9ddd-f6d3772d6873"><br>
**Inputs:**<br>
- frame_index - INT<br>

**Outputs:**<br>
- last_decoded_frame - INT<br>
<hr>

## Decoded Frame History (UI)<br>
Displays the last few decoded Frames - only UI, no saving of decoded frame numbers<br>
<img src="https://github.com/user-attachments/assets/8f2b3c03-2038-49a2-a621-5d7e22584214"><br>
**Inputs:**<br>
- frame_index - INT<br>

**Outputs:**<br>
- decoded_frames - STRING<br>
<hr>

## WAN Latent Slice<br>
Allows you to slice a loaded latent in more chunks.<br>
<img src="https://github.com/user-attachments/assets/e81e7f3f-c474-4a15-84a3-a9683d36e88c"><br>
**Inputs:**<br>
- latent - LATENT<br>
- Start - INT<br>
- Stop - INT<br>

**Outputs:**<br>
- latent - LATENT<br>
<hr>

## NHWC -> NCHW (ONNX Fix)<br>
Normalizes the image tensor layout by converting NHWC to NCHW and back to ensure compatibility with certain backends and models, without altering the image data.<br>
<img src="https://github.com/user-attachments/assets/dbfac63c-a69b-441c-bde6-61d99e599747"><br>
**Inputs:**<br>
- image - IMAGE<br>

**Outputs:**<br>
- IMAGE - IMAGE<br>
<hr>


## A1111-compatible image saving<br>
Custom image-save node.<br>
Allow saving images including configuration-data. Images saved with proper filled metadata can be loaded cirectly into Stability-Matrix with all settings pre-filled.
Used LoRA are not (yet) saved as Metadata.
<img src="https://github.com/user-attachments/assets/40812ed7-8603-49e3-ad0c-c7c28f2cae65"><br>
**Inputs:**<br>
- images - IMAGE<br>
- positive - STRING<br>
- negative - STRING<br>
- steps - INT<br>
- sampler - STRING<br>
- scheduler - STRING<br>
- cfg - FLOAT<br>
- seed - INT<br>
- width - INT<br>
- height - INT<br>
- model_name - STRING<br>
- model_hash - STRING<br>
- filename - STRING<br>
- output_path - STRING<br>

**Outputs:**<br>
none
<hr>



