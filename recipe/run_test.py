import platform

# import astropy._compiler
import astropy.cosmology.flrw.scalar_inv_efuncs
import astropy.io.ascii.cparser
import astropy.io.votable.tablewriter
import astropy.modeling.projections
import astropy.timeseries.periodograms.lombscargle.implementations.cython_impl
import astropy.table._column_mixins
import astropy.table._np_utils
import astropy.utils._compiler
import astropy.utils.xml._iterparser
import astropy.wcs._wcs

# We run a subset of the tests which are the most likely to have
# issues because they rely on C extensions and bundled libraries

from astropy import test


if platform.machine() in ('aarch64', 'ppc64le'):
    print('WARNING: Skipping most tests on aarch64/ppc64le because they take too long')
    test(package='wcs')
    test(package='io.fits')
else:
    test()
