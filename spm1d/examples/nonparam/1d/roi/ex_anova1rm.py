
import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load dataset:
dataset      = spm1d.data.uv1d.anova1rm.SpeedGRFcategoricalRM()
y,A,SUBJ     = dataset.get_data()

#(0a) Create region of interest(ROI):
roi        = np.array( [False]*y.shape[1] )
roi[25:45] = True


#(1) Conduct non-parametric test:
np.random.seed(0)
alpha      = 0.05
snpm       = spm1d.stats.nonparam.anova1rm(y, A, SUBJ, roi=roi)
snpmi      = snpm.inference(alpha, iterations=500)
print( snpmi )




#(2) Compare with parametric result:
spm        = spm1d.stats.anova1rm(y, A, SUBJ, equal_var=True, roi=roi)
spmi       = spm.inference(alpha)
print( spmi )




#(3) Plot
pyplot.close('all')
pyplot.figure(figsize=(12,4))

ax0 = pyplot.subplot(121)
ax1 = pyplot.subplot(122)
labels = 'Parametric', 'Non-parametric'
for ax,zi,label in zip([ax0,ax1], [spmi,snpmi], labels):
	zi.plot(ax=ax)
	zi.plot_threshold_label(ax=ax, fontsize=8)
	zi.plot_p_values(ax=ax, size=10)
	ax.set_title( label )
pyplot.show()


