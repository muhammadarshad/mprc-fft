# Upstream research source

Authoritative upstream repository:

https://github.com/muhammadarshad/mprc-learn-train

Pinned research snapshot:

`b02cf411719721b5e737a9601f253f7db080d0a8`

This directory in `mprc-fft` is a downstream integration/vendor location only. New learning/training experiments, datasets, reproducibility scripts, and result provenance belong upstream first.

Current upstream reproduces:

- exhaustive W²/B¹ Z256 test;
- real handwritten-digit LoG -> Z256 -> LUT training;
- local + stride-7 relation learning;
- Arshad's ViT ADI-9 / walk-7 ablations;
- VOF integer-second-difference ablation;
- conventional GD controls on the same empirical split.

Do not edit the research history here first. Promote a tested upstream commit, then update this pin.
