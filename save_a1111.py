import os
import json
import time
import numpy as np
from PIL import Image, PngImagePlugin

class SaveImageA1111:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),

                "positive": ("STRING",),
                "negative": ("STRING",),

                "steps": ("INT",),
                "sampler": ("STRING",),      # UI-Name! z.B. "Euler Ancestral Karras"
                "scheduler": ("STRING",),    # z.B. "karras"
                "cfg": ("FLOAT",),
                "seed": ("INT",),

                "width": ("INT",),
                "height": ("INT",),

                "model_name": ("STRING",),
                "model_hash": ("STRING",),

                "filename": ("STRING",),     # frei wählbarer Name
                "output_path": ("STRING",),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "save"
    OUTPUT_NODE = True
    CATEGORY = "image/save"

    def save(
        self,
        images,
        positive,
        negative,
        steps,
        sampler,
        scheduler,
        cfg,
        seed,
        width,
        height,
        model_name,
        model_hash,
        filename,
        output_path
    ):
        os.makedirs(output_path, exist_ok=True)

        for i, image in enumerate(images):
            img_np = image.cpu().numpy()
            img_np = (img_np * 255).clip(0, 255).astype(np.uint8)
            img = Image.fromarray(img_np)

            info = PngImagePlugin.PngInfo()

            # --------------------------------------------------
            # parameters (A1111 classic)
            # --------------------------------------------------
            parameters_text = (
                f"{positive}\n"
                f"Negative prompt: {negative}\n"
                f"Steps: {steps}, "
                f"Sampler: {sampler}, "
                f"CFG scale: {cfg}, "
                f"Seed: {seed}, "
                f"Size: {width}x{height}, "
                f"Model hash: {model_hash}, "
                f"Model: {model_name}"
            )

            info.add_text("parameters", parameters_text)

            # --------------------------------------------------
            # parameters-json (Stability Matrix compatible)
            # --------------------------------------------------
            parameters_json = {
                "PositivePrompt": positive,
                "NegativePrompt": negative,
                "Steps": steps,
                "Sampler": sampler,
                "CfgScale": cfg,
                "Seed": seed,
                "Width": width,
                "Height": height,
                "ModelName": model_name,
                "ModelHash": model_hash,

                # Pflichtfelder (auch wenn leer)
                "FrameCount": 0,
                "MotionBucketId": 0,
                "VideoQuality": 0,
                "Lossless": False,
                "Fps": 0,
                "OutputFps": 0,
                "MinCfg": 0,
                "AugmentationLevel": 0,
                "VideoOutputMethod": None,
                "ModelVersionId": None,
                "ExtraNetworkModelVersionIds": None,
            }

            info.add_text(
                "parameters-json",
                json.dumps(parameters_json, ensure_ascii=False)
            )

            # --------------------------------------------------
            # smproj (DER Schlüssel für Stability Matrix)
            # --------------------------------------------------
            smproj = {
                "Version": 2,
                "ProjectType": "TextToImage",
                "State": {
                    "Model": {
                        "SelectedModelName": model_name
                    },
                    "Sampler": {
                        "Steps": steps,
                        "CfgScale": cfg,
                        "Width": width,
                        "Height": height,
                        "SelectedSampler": {
                            "Name": sampler.lower().replace(" ", "_")
                        },
                        "SelectedScheduler": {
                            "Name": scheduler.lower()
                        }
                    },
                    "Prompt": {
                        "Prompt": positive,
                        "NegativePrompt": negative
                    },
                    "Seed": {
                        "Seed": str(seed),
                        "IsRandomizeEnabled": False
                    }
                }
            }

            info.add_text(
                "smproj",
                json.dumps(smproj, ensure_ascii=False)
            )

            # --------------------------------------------------
            # Filename: <name>_0000.png
            # --------------------------------------------------
            final_name = f"{filename}_{i:04d}.png"
            full_path = os.path.join(output_path, final_name)

            img.save(full_path, pnginfo=info)

        return ()