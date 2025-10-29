# Sora Generates Videos with Stunning Geometrical Consistency
Generates Videos  Geometrical Consistency metric toolbox (GVGC metric)
##
The recently developed Sora model [1] has exhibited remarkable capabilities in video generation, sparking intense discussions regarding its ability to simulate real-world phenomena. Despite its growing popularity, there is a lack of established metrics to quantitatively evaluate its fidelity to real-world physics. In this paper, we introduce a new benchmark that assesses the quality of the generated videos based on their adherence to real-world physics principles. We employ a method that transforms the generated videos to 3D models, leveraging the premise that the accuracy of 3D reconstruction is heavily contingent on the video quality. From the perspective of 3D reconstruction, we use the fidelity of the geometric constraints satisfied by the constructed 3D models as a proxy to gauge the extent to which the generated videos conform to the rules of real-world physics.
## Homepase
https://sora-geometrical-consistency.github.io/
## Fast forward
<div align="left">
 <img src="img/teaser.png" width="80%">
</div>

<div align="left">
 <img src="img/fidelitymetric.png" width="80%">
</div>

<div align="left">
 <img src="img/stereomatching.png" width="80%">
</div>

<div align="left">
 <img src="img/matching.png" width="80%">
</div>


<div align="left">
 <img src="img/recon.png" width="80%">
</div>


## Data
### data download link:
https://drive.google.com/file/d/1E_7DR_DIvvWtDXn5KXUwXfBIA_3MhBMG/view?usp=drive_link
place the data file as fllows:
```python
root
|
---xxx.py
---XXX.py
---data
   |
   ---sora
   |
   ---gen2
   |
   ---pika
```
## Code

### Requirements
```bash
pip install opencv-python numpy
```

### Code Usage

#### Command Line Interface (Recommended)

Evaluate a single output video:
```bash
python Eval_all.py --output_video yucheng
```

Evaluate output video with ground truth comparison:
```bash
python Eval_all.py --output_video yucheng --gt_video gt
```



### Command Line Arguments

- `--output_video`: (Required) Name of the output video folder to evaluate (e.g., "yucheng", "sora", "pika")
- `--gt_video`: (Optional) Name of the ground truth video folder for comparison (e.g., "gt")

### Input Data Structure

Your video files should be organized as follows:
```
data/
├── your_video_name/
│   └── video_file.mp4
├── gt/  (optional, for ground truth)
│   └── gt_video_file.mp4
```

## Results

### Output Structure

After running the evaluation, results will be organized as follows:

```
data/
├── your_video_name/
│   ├── frame_images/              # Extracted video frames
│   │   └── video_name/
│   │       ├── frame_0.png
│   │       ├── frame_1.png
│   │       └── ...
│   ├── brief_result/              # Summary metrics (CSV files)
│   │   └── 60_3_err_whole.csv    # Overall evaluation metrics
│   ├── full_result/               # Detailed per-frame results
│   │   └── video_name/
│   │       └── 60_3_err.csv      # Frame-by-frame error metrics
│   ├── image_result/              # Visualization images
│   │   └── video_name/
│   │       ├── matching_*.png    # Feature matching visualizations
│   │       └── depth_*.png       # Depth map visualizations
│   └── info.csv                   # Video metadata (fps, frames, etc.)
```

### Understanding the Results

#### Brief Result Files (`brief_result/`)
- **File format**: `{interval}_{ransac_threshold}_err_whole.csv`
- **Content**: Aggregated metrics across all frame pairs
- **Columns**:
  - `data_name`: Video name
  - `mean_error`: Average epipolar geometry error
  - `median_error`: Median error
  - `rmse`: Root mean squared error
  - `mae`: Mean absolute error
  - `keep_rate`: Percentage of inlier matches (higher = better geometric consistency)
  - `num_inliers_F`: Average number of valid feature matches
  - `num_pts`: Average total number of feature points

#### Full Result Files (`full_result/`)
- **File format**: `{interval}_{ransac_threshold}_err.csv`
- **Content**: Detailed metrics for each frame pair
- **Columns**: Same as brief result, but per frame pair

#### Key Metrics
- **Lower error values** (mean_error, rmse, mae) = Better geometric consistency
- **Higher keep_rate** (closer to 1.0) = More geometrically consistent video
- **More num_inliers_F** = Better feature matching quality

### Example Results Interpretation

```csv
data_name,mean_error,median_error,rmse,mae,keep_rate,num_inliers_F,num_pts
Yucheng 2025-10-10 16.16.16,2.5,2.1,3.2,2.5,0.85,1500,1800
```

This means:
- The video has an average epipolar error of 2.5 pixels
- 85% of feature matches satisfy geometric constraints (good consistency)
- Successfully matched 1500 valid point correspondences per frame pair
## Media report
用 Sora 影片建 3D！ https://www.youtube.com/watch?v=X6n5ZCc7yy0 

