
import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load dataset:
# dataset      = spm1d.data.mv1d.hotellings_paired.Neptune1999kneekin()
dataset      = spm1d.data.mv1d.hotellings_paired.Pataky2014cop()
yA,yB        = dataset.get_data()  #A:slow, B:fast



#(1) Conduct non-parametric test:
np.random.seed(0)
alpha      = 0.05
snpm       = spm1d.stats.nonparam.hotellings_paired(yA, yB)
snpmi      = snpm.inference(alpha, iterations=100)
print( snpmi )




#(2) Compare with parametric result:
spm        = spm1d.stats.hotellings_paired(yA, yB)
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


