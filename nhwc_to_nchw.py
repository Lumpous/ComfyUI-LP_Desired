import torch

class NHWC_to_NCHW:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "convert"
    CATEGORY = "image/convert"

    def convert(self, image):
        # image: [B, H, W, C]
        x = image.permute(0, 3, 1, 2)  # -> NCHW
        x = x.permute(0, 2, 3, 1)      # zurück zu IMAGE-kompatibel
        return (x,)