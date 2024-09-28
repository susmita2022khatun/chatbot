# test_pytorch.py
try:
    import torch
    print("PyTorch version:", torch.__version__)
except AttributeError as e:
    print(f"Error: {e}")
