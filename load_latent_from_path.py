import os
import hashlib
import torch
import safetensors.torch
import folder_paths


class LoadLatentFromPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent_path": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "load"
    CATEGORY = "latents"

    def load(self, latent_path):
        if not os.path.exists(latent_path):
            raise FileNotFoundError(f"Latent file not found: {latent_path}")

        latent = safetensors.torch.load_file(latent_path, device="cpu")

        multiplier = 1.0
        if "latent_format_version_0" not in latent:
            multiplier = 1.0 / 0.18215

        samples = {
            "samples": latent["latent_tensor"].float() * multiplier
        }
        return (samples,)

    @classmethod
    def IS_CHANGED(cls, latent_path):
        if not os.path.exists(latent_path):
            return ""
        m = hashlib.sha256()
        with open(latent_path, "rb") as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(cls, latent_path):
        if not os.path.exists(latent_path):
            return f"Invalid latent file: {latent_path}"
        return True


class LatentFrameCount:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("frame_count",)
    FUNCTION = "count"
    CATEGORY = "latents"

    def count(self, latent):
        tensor = latent["samples"]

        # WAN: entweder [T, C, H, W] oder [1, T, C, H, W]
        if tensor.dim() == 5:
            frame_count = tensor.shape[2]
        else:
            frame_count = tensor.shape[0]

        return (int(frame_count),)


class LastDecodedFrameUI:
    _last_value = None  # UI-Lebensdauer-State

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frame_index": ("INT",),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("last_decoded_frame",)
    FUNCTION = "log"
    CATEGORY = "latents"

    def log(self, frame_index):
        # Wird NUR aufgerufen, wenn der Flow wirklich ausgeführt wird
        LastDecodedFrameUI._last_value = int(frame_index)
        return (LastDecodedFrameUI._last_value,)
		
		
class DecodedFrameHistoryUI:
    _history = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frame_index": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("decoded_frames",)
    FUNCTION = "log"
    CATEGORY = "latents"

    def log(self, frame_index):
        # None-safe: wenn Input fehlt, einfach History nicht ändern
        if frame_index is None:
            text = "\n".join(str(i) for i in reversed(self._history))
            return (text,)

        fi = int(frame_index)

        # optional: Duplikate direkt hintereinander vermeiden
        if not self._history or self._history[-1] != fi:
            self._history.append(fi)

        text = "\n".join(str(i) for i in reversed(self._history))
        return (text,)


class WanLatentSlice:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "start": ("INT", {"default": 0}),
                "stop": ("INT", {"default": 1}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "slice"
    CATEGORY = "latents"

    def slice(self, latent, start, stop):
        samples = latent["samples"]

        # WAN layout: [B, C, T, H, W]
        if samples.dim() != 5:
            raise ValueError(f"Unexpected WAN latent shape: {samples.shape}")

        sliced = samples[:, :, start:stop, :, :]

        if sliced.shape[2] == 0:
            raise ValueError(f"Empty time slice: start={start}, stop={stop}")

        return ({"samples": sliced.clone()},)