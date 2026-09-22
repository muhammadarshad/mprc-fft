# Upstream research source

Authoritative upstream repository:

https://github.com/muhammadarshad/mprc-learn-train

Pinned research snapshot:

`ffafa12ff5131f14fe6fa656bb5ede00310d07d9`

This directory in `mprc-fft` is a downstream integration/vendor location only. New learning/training experiments, datasets, reproducibility scripts, and result provenance belong upstream first.

Current upstream reproduces:

- exhaustive W²/B¹ Z256 test;
- real handwritten-digit LoG -> Z256 -> LUT training;
- local + stride-7 relation learning;
- Arshad's ViT ADI-9 / walk-7 ablations;
- VOF integer-second-difference ablation;
- conventional GD controls on the same empirical split.

Do not edit the research history here first. Promote a tested upstream commit, then update this pin.
