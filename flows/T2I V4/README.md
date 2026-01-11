## (File: T2I V4.1f.json)<br>

 [T2I V4](./T2I%20V4/) 

Requirements:<br>
[ComfyUI-LP_Desired](https://github.com/Lumpous/ComfyUI-LP_Desired)<br>
[rgthree-comfy](https://github.com/rgthree/rgthree-comfy)<br>
[ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)<br>
[ComfyUI_RyanOnTheInside](https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside)<br>
[ComfyUI-Basic-Math](https://github.com/akatz-ai/ComfyUI-Basic-Math)<br>
[ComfyMath](https://github.com/evanspearman/ComfyMath)<br>
[ComfyUI-WildPromptor](https://github.com/1038lab/ComfyUI-WildPromptor)<br>
[ComfyUI-stable-wildcards](https://github.com/DigitalIO/ComfyUI-stable-wildcards)<br>
[ComfyUI-Impact-Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack)<br>
[ComfyUI_StringEssentials](https://github.com/bradsec/ComfyUI_StringEssentials)<br>
[ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)<br>
[ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)<br>
[ComfyUI-String-Helper](https://github.com/liuqianhonga/ComfyUI-String-Helper)<br>
[ComfyUI-WildPromptor](https://github.com/1038lab/ComfyUI-WildPromptor)<br>

## The full T2I workflow includes the following key sections:<br>
<br>

## Seed Selection (Noise & Variance)<br>
<img width="275" height="478" alt="image" src="https://github.com/user-attachments/assets/81a31372-461d-4c6b-9815-3b346c2bb97e" /><br>
**Top:**<br>
- <noise_seed><br>
Base seed used for generation.

**Middle:**<br>
- Used only when <noise_seed> is fixed.<br>
- Leave at <0> when using a fully fixed seed.<br>
- Can be used to increment or decrement the seed by a fixed value.<br>

**Bottom:**<br>
- Used only when noise_seed is fixed.<br>
- Adds very small additional noise to the base seed.<br>
- Allows tiny variations without changing the actual seed value.<br>

<hr>
<br>

## KSampler Configuration<br>
<img width="301" height="261" alt="image" src="https://github.com/user-attachments/assets/b4808752-5d36-41d1-b586-ced76243d1c6" /><br>
This workflow uses three samplers, so step configuration is critical.<br>
Incorrect step ranges will negatively affect results.<br>

Sampler 1:<br>
- Runs from step 0 to <refiner_step> (e.g. 0-24)<br>
  
Sampler 2:<br>
- Runs from <refiner_step> to <steps_total> (e.g. 24-34)<br>

Sampler 2:<br>
- Reprocesses the final step only (e.g. 33-34)<br>

<hr>
<br>

## Image Resolution & Batch Size<br>
<img width="767" height="403" alt="image" src="https://github.com/user-attachments/assets/af0288ac-f158-4993-a374-a642b77ff896" /><br>
Predefined image resolutions can be selected by changing the <Size Index> value.<br>

<hr>
<br>

## Postprocessings<br>
<img width="768" height="476" alt="image" src="https://github.com/user-attachments/assets/5f2b630d-0331-4507-94ed-bafcc67e6069" /><br>
The workflow currently includes three post-processing stages:<br>
Background Softening:<br>
- Uses the Flex Image Tilt Shift node by RyanOnTheInside<br>
- Fixed settings for consistent results<br>
<img width="266" height="488" alt="image" src="https://github.com/user-attachments/assets/5afb3e78-68cc-459d-b681-067dc268428f" /><br>

Cinematic Selector:<br>
Applies contrast and brightness using predefined presets:<br>
- Contrast 0.9 + Brightness 0.95<br>
- Contrast 1.0 + Brightness 1.0<br>
- Contrast 1.15 + Brightness 1.05<br>

Focus Selector:<br>
Applies contrast-only adjustments:<br>
- Contrast 0.9<br>
- Contrast 1.0<br>
- Contrast 1.1<br>

<hr>
<br>

## Horizontal & Vertical Tilt-Shift<br>
<img width="575" height="377" alt="image" src="https://github.com/user-attachments/assets/84e6cc6a-b59c-480f-9b3e-ff7bcba8e6f3" />
<img width="572" height="377" alt="image" src="https://github.com/user-attachments/assets/42bcc9d4-11ac-4003-ae6c-32e7d429bea0" /><br>
2 variances of Tilt-Shift effects are included, Horizontal and vertical<br>
Implemented by generating a mask on the fly applying it to the image.

# important note: center clearance is the size of the area form images center where the mask is NOT applied to!<br>
(e.g. the black area seen below is center clearance)<br>
<img width="1070" height="303" alt="image" src="https://github.com/user-attachments/assets/b8b0a80a-d5ca-414f-8e37-5ad8af54c9e5" /><br>

<hr>
<br>

## Upscaling<br>
<img width="633" height="244" alt="image" src="https://github.com/user-attachments/assets/184ec5fa-ff54-4162-bbce-4ca5760b197d" /><br>
The workflow includes 5 different upscaling methods, selectable depending on output target and performance constraints.<br>
<br>
<hr>








