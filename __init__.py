from .load_latent_from_path import (
    LoadLatentFromPath,
    LatentFrameCount,
    LastDecodedFrameUI,
    DecodedFrameHistoryUI,
    WanLatentSlice
)

from .nhwc_to_nchw import (
    NHWC_to_NCHW
)

from .save_a1111 import (
    SaveImageA1111
)
NODE_CLASS_MAPPINGS = {
    "LoadLatentFromPath": LoadLatentFromPath,
	"LatentFrameCount": LatentFrameCount,
	"LastDecodedFrameUI": LastDecodedFrameUI,
	"DecodedFrameHistoryUI": DecodedFrameHistoryUI,
	"WanLatentSlice": WanLatentSlice,
	"NHWC_to_NCHW": NHWC_to_NCHW,
	"SaveImageA1111": SaveImageA1111
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadLatentFromPath": "Load Latent (Path)",
	"LatentFrameCount": "Latent Frame Count",
	"LastDecodedFrameUI": "Last Decoded Frame (UI)",
	"DecodedFrameHistoryUI": "Decoded Frame History (UI)",
	"WanLatentSlice": "WAN Latent Slice",
	"NHWC_to_NCHW": "NHWC → NCHW (ONNX Fix)",
	"SaveImageA1111": "Save Image (A1111 + Stability Matrix)"
}