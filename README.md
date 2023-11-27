
# LDA Topic Modeling for News

The aim of this project is to examine the separation of contents in the [Bloomberg Quint news dataset](https://data.world/crawlfeeds/bloomberg-quint-news-dataset) into topics using LDA. 

The project includes:
- cleaning the dataset (removing empty content)
- discarding words/word groups that will create pollution with regex
- selecting the parameters that make the model most successful in terms of `coherence score` and `perplexity` metrics with grid search
- making live visualizations of the subjects reduced in size with pyLDAvis
- preprocessing and LDA model training times
- measuring and visualizing the metric success of the model for different parameters.

External libraries and packages:
- Gensim for LDA
- NLTK
- Pandas
- pyLDAvis
- Matplotlib
- NumPy
- Re 



## Screenshots
![pyLDAvis Visualization](https://raw.githubusercontent.com/robuno/LDA_TopicModeling_for_News/master/results/vis_intertopic_dist.png)

![3D Scatter Plot of Coherence Score (a:auto)](https://raw.githubusercontent.com/robuno/LDA_TopicModeling_for_News/master/results/3d_scatter_alpha_auto.png)

![3D Scatter Plot of Coherence Score (a:symmetric)](https://raw.githubusercontent.com/robuno/LDA_TopicModeling_for_News/master/results/3d_scatter_alpha_sym.png)





  
## Results

| ID |   Number of Topics |   Chunk Size |   Number of Passes | Alpha     |     Time |   Perplexity |   Coherence Score |
|---:|-------------------:|-------------:|-------------------:|:----------|---------:|-------------:|------------------:|
|  0 |                  8 |           50 |                 50 | symmetric |  439.219 |     -8.97722 |          0.443384 |
|  1 |                  8 |           50 |                150 | symmetric | 1318.87  |     -8.91857 |          0.444481 |
|  2 |                  8 |          200 |                 50 | symmetric |  265.116 |     -8.75447 |          0.460507 |
|  3 |                  8 |          200 |                150 | symmetric |  788.782 |     -8.69654 |          0.455662 |
|  4 |                 12 |           50 |                 50 | symmetric |  605.328 |    -10.6225  |          0.466916 |
|  5 |                 12 |           50 |                150 | symmetric | 1841.27  |    -10.6042  |          0.470954 |
|  6 |                 12 |          200 |                 50 | symmetric |  327.599 |     -9.89892 |          0.499482 |
|  7 |                 12 |          200 |                150 | symmetric |  987.428 |     -9.8809  |          0.49409  |
|  8 |                  8 |           50 |                 50 | auto      |  430.904 |     -8.96813 |          0.436378 |
|  9 |                  8 |           50 |                150 | auto      | 1294.23  |     -8.90955 |          0.446728 |
| 10 |                  8 |          200 |                 50 | auto      |  262.156 |     -8.75042 |          0.457758 |
| 11 |                  8 |          200 |                150 | auto      |  775.119 |     -8.69211 |          0.465276 |
| 12 |                 12 |           50 |                 50 | auto      |  602.978 |    -10.607   |          0.455874 |
| 13 |                 12 |           50 |                150 | auto      | 1785.82  |    -10.5896  |          0.462043 |
| 14 |                 12 |          200 |                 50 | auto      |  326.369 |     -9.89271 |          0.504308 |
| 15 |                 12 |          200 |                150 | auto      |  975.203 |     -9.87507 |          0.498671 |


## Results (descending by coherence score)
| ID|   Number of Topics |   Chunk Size |   Number of Passes | Alpha     |     Time |   Perplexity |   Coherence Score |
|---:|-------------------:|-------------:|-------------------:|:----------|---------:|-------------:|------------------:|
| 14 |                 12 |          200 |                 50 | auto      |  326.369 |     -9.89271 |          0.504308 |
|  6 |                 12 |          200 |                 50 | symmetric |  327.599 |     -9.89892 |          0.499482 |
| 15 |                 12 |          200 |                150 | auto      |  975.203 |     -9.87507 |          0.498671 |
|  7 |                 12 |          200 |                150 | symmetric |  987.428 |     -9.8809  |          0.49409  |
|  5 |                 12 |           50 |                150 | symmetric | 1841.27  |    -10.6042  |          0.470954 |
|  4 |                 12 |           50 |                 50 | symmetric |  605.328 |    -10.6225  |          0.466916 |
| 11 |                  8 |          200 |                150 | auto      |  775.119 |     -8.69211 |          0.465276 |
| 13 |                 12 |           50 |                150 | auto      | 1785.82  |    -10.5896  |          0.462043 |
|  2 |                  8 |          200 |                 50 | symmetric |  265.116 |     -8.75447 |          0.460507 |
| 10 |                  8 |          200 |                 50 | auto      |  262.156 |     -8.75042 |          0.457758 |
| 12 |                 12 |           50 |                 50 | auto      |  602.978 |    -10.607   |          0.455874 |
|  3 |                  8 |          200 |                150 | symmetric |  788.782 |     -8.69654 |          0.455662 |
|  9 |                  8 |           50 |                150 | auto      | 1294.23  |     -8.90955 |          0.446728 |
|  1 |                  8 |           50 |                150 | symmetric | 1318.87  |     -8.91857 |          0.444481 |
|  0 |                  8 |           50 |                 50 | symmetric |  439.219 |     -8.97722 |          0.443384 |
|  8 |                  8 |           50 |                 50 | auto      |  430.904 |     -8.96813 |          0.436378 |


## Elapsed Time Spent on LDA Training
![Elapsed Time Spent on LDA Training](https://raw.githubusercontent.com/robuno/LDA_TopicModeling_for_News/master/results/time_hole_pie.png)