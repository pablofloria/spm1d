
import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load dataset:
dataset    = spm1d.data.uv1d.anova1.SpeedGRFcategorical()
# dataset    = spm1d.data.uv1d.anova1.Weather()
y,A        = dataset.get_data()

#(0a) Create region of interest(ROI):
roi        = np.array( [False]*y.shape[1] )
roi[15:75] = True


# #(1) Conduct non-parametric test:
np.random.seed(0)
alpha      = 0.05
snpm       = spm1d.stats.nonparam.anova1(y, A, roi=roi)
snpmi      = snpm.inference(alpha, iterations=200)
print snpmi




#(2) Compare with parametric result:
spm        = spm1d.stats.anova1(y, A, equal_var=True, roi=roi)
spmi       = spm.inference(alpha)
print spmi




#(3) Plot
pyplot.close('all')
pyplot.figure(figsize=(12,4))
pyplot.get_current_fig_manager().window.move(0, 0)
ax0 = pyplot.subplot(121)
ax1 = pyplot.subplot(122)
labels = 'Parametric', 'Non-parametric'
for ax,zi,label in zip([ax0,ax1], [spmi,snpmi], labels):
	zi.plot(ax=ax)
	zi.plot_threshold_label(ax=ax, fontsize=8)
	zi.plot_p_values(ax=ax, size=10)
	ax.set_title( label )
pyplot.show()
