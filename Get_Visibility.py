# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:03:28 2018

@author: w9641432
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:54:05 2018

@author: w9641432
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:52:11 2018

@author: Ajones

"""

# Consult:  "Formation and evolution mechanism of regional haze:
# a case study in the megacity Beijing, China"
# doi:10.5194/acp-13-4501-2013
# X. G. Liu et al

import sys


def AQI2PM(aqi):
    
    # calculation of pm from AQI value (US standard model)
    
    if aqi >= 0 and aqi <=50:
        
        PMmin = 0
        PMmax = 12
        aqilower = 0
        aqiupper = 50
        aqival = aqi
   
    elif aqi > 50 and aqi <=100:
        
        PMmin = 12.1
        PMmax = 35.4
        aqilower = 50
        aqiupper = 100
        aqival = aqi
    
    elif aqi > 100 and aqi <=150:
        
        PMmin = 35.5
        PMmax = 55.4
        aqilower = 100
        aqiupper = 150
        aqival = aqi
        
    elif aqi > 150 and aqi <=200:
        
        PMmin = 55.5
        PMmax = 150.4
        aqilower = 150
        aqiupper = 200
        aqival = aqi
        
    elif aqi > 200 and aqi <=300:
        
        PMmin = 150.5
        PMmax = 250.4
        aqilower = 200
        aqiupper = 300
        aqival = aqi 
        
    elif aqi > 300 and aqi <=400:
        
        PMmin = 250.5
        PMmax = 350.4
        aqilower = 300
        aqiupper = 400
        aqival = aqi     

    elif aqi > 400 and aqi <=500:
        
        PMmin = 350.5
        PMmax = 500
        aqilower = 400
        aqiupper = 500
        aqival = aqi     
    
    
    Bpmax = (((aqival - aqilower) * (PMmax - PMmin)) / (aqiupper- aqilower)) + PMmin
    return Bpmax

def visibility(td,tw,aqi,pm):
    
    # Check inputs
    if (pm == -1) & (aqi != -1):
    # calculate pm25 value based off AQI value
        pm = AQI2PM(aqi)
    elif (aqi==-1) & (pm !=-1):
    # PM2.5 value as is    
        pm = pm
    elif (aqi==-1) & (pm ==-1):
    # Error    
        print('Error in inputs. Please try again')
        sys.exit()
    
    print('PM2.5 = ' + str(pm))
    
    Qsp = 5.3
    Qap = 0.6
    a   = 4.77
    b   = 7.12 

    # relative humidity pre calcs, When above -20C use if statement, below -20C, use else statement
    if td>=-20:
        ed = 6.116441*10**((7.591386*td)/(td+240.7263)) # actual vapur density
        ew = 6.116441*10**((7.591386*tw)/(tw+240.7263)) # saturation vapour density
    else:
        ed = 6.114742*10**((9.778707*td)/(td+273.1466)) # actual vapur density
        ew = 6.114742*10**((9.778707*tw)/(tw+273.1466)) # saturation vapour density
    
    # Relative humidity value
    rh = (ew/ed)*100
    
    
         
    print('RH: ' + str(rh))
    # visibility equation
    vis = -(-(3.912 / (Qsp * pm * (1+ a * (rh/100) ** b) + Qap * pm + 24)) * 1000) 
    # Suggested visibility to set
            
    print('Visibility = ' + str(round(vis)) + ' km')
        
    return pm,rh,vis


# enter Td,Tw, AQI (if known) set to -1 if not, pm (if known) set -1 if not
[Pm25,Rh,vis] = visibility(23,17,33,-1)
