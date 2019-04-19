import numpy as np
import pdb 


Rd   = 287.                         # Gas constant for dry air, J/(kg K)
Rv   = 461.6                        # Gas constant for water vapor, J/(kg K)
cp   = 7.*0.5*Rd                    # Specific heat of dry air at constant pressure, J/(kg K)
cv   = cp - Rd                      # Specific heat of dry air at constant volume, J/(kg K)
pref = 100000.0                     # reference sea level pressure, Pa
g    = 9.81                         # gravitational constant (m/s^2)


def vap_pres(r,p):
    # compute water vapor pressure using mixing ratio (r, in kg/kg) and pressure (p, in Pa):
    e = r*p/((Rd/Rv)+r)
    return e

def esat( t ):
    # compute saturation vapor pressure based on temperature (in K). Output is in Pa.
    # WMO reference formula is that of Goff and Gratch (1946), slightly
    # modified by Goff in 1965:
    e1=101325.0
    TK=273.15
    esat = e1*np.power(10,(10.79586*(1-TK/t)-5.02808*np.log10(t/TK) + 1.50474*1e-4*(1-np.power(10,(-8.29692*(t/TK-1))))+0.42873*1e-3*(np.power(10,(4.76955*(1-TK/t)))-1)-2.2195983))
    return esat

def relhum( t, p, r ):
    # compute relative humidity based on temperature (t, in K),
    # pressure (p in Pa) and mixing ratio (r, in kg/kg):
    rh = vap_pres(r,p)/esat(t)
    return rh

def Tsat( r ):
    # compute saturation temperature from the mixing ratio (in kg/kg)
    r[np.where(r<1e-10000)] = np.nan
    r = r*1e3 # convert to g/kg
    tsat = 255.33 + 12.46*np.log(r*(1.0+.0265*r))
    return tsat

def theta_e( theta, r ):
    # compute equivalent potential temperature using potential temperature and mixing ratio:
    epott = theta*np.exp((3.376/Tsat(r)-.00254)*r*(1.0+.00081*r))
    #else:
    #   epott = np.nan
    return epott

np.arctan(1)
def wb(t, rh):

    # Compute wet bulb from temperature (t) in °C and relativity humidity RH%
    # https://journals.ametsoc.org/doi/pdf/10.1175/JAMC-D-11-0143.1

    pdb.set_trace()
    rh = t*np.arctan(0.151977*(rh + 8.313659)**(1/2)) + np.arctan(t + rh) - np.arctan(rh - 1.676331
            ) + 0.00391838*(rh)**(3/2) * np.arctan(0.023101 * rh) - 4.686035
    return(rh)
wb(20,50)
