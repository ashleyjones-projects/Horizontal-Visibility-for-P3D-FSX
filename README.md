# Visibility
Model that estimates horizontal visibility given various atmospheric parameters

This algorithm estimates horizontal visibility which is intended for flight simulation packages, such as P3D and FSX, and their weather applications, but can also be used for general purpose. Firstly, the model used here is not my own, but that of various scientific studies that devised a machine learning algorithm using PM2.5 and visibility measurements taken by various instruments in the city of Beijing, China. Please see Liu et al., [2013] for a full description and model details. Visibility is dependent upon various factors, including: the intensity of light, relative humidity, and pollution. Intensity of light here is irrelevant here as I am interested in the effects of how light is attenuated due to physical properties of the atmosphere. I.e., you can still have good visibility at night even though it’s dark! Particles and pollution in general (such as ozone, sulphates, nitrates, particulate organic matter etc..) play a major part in attenuating light by scattering or absorbing light radiation along the path it travels. The amount of light extinction is dependent upon many physical, chemical, electrical, and optical properties of these pollutants. This model uses Particulate Matter at 2.5 microns (PM2.5) as a gauge for light extinction. Another important factor is relative humidity (RH), which is the ratio between the actual vapour density and saturation vapour density (in g/m3) and can be calculated using the Dry-bulb temperature (Td) and dew-point temperature (Tw). Relative humidity is the amount of moisture in the air compared to what the air can "hold" at that temperature. When the air can't "hold" all the moisture, then it condenses as dew. As the RH increases, it augments the hygroscopic properties of the particles, making them grow in size and hence, augmenting light extinction. When the horizontal visibility is <=10 km and the RH >90%, it is referred to as haze.  

I have tested the model using landmarks in the city to which I live and it has shown to be fairly accurate (+/- 5km) given the uncertainties in the model, weather data provided, and also in my own observations. I have used airport Metar data to use as inputs for Td and Tw. PM2.5 values are acquirable from various sites, such as https://www.airvisual.com. The model uses Eq 1. and Eq 5 from the Liu et al., paper. Figure 12 shows a nice example of estimated visibility as a function PM2.5 for various RH values. It should be noted also that I have used the upper bounds of uncertainty for the coefficient values as I feel the both weather simulations in P3D/FSX tend to over exaggerate visibility reduction. However, the variance in the ratio of wet to dry light scattering acting as a function of RH is favourable. R2-values show that 93% of the variability in Hygroscopic growth can be explained by RH (see Fig 11.), owing to not significantly large differences in visibility reduction if using the average coefficient values (< +/- 1km).

The inputs are as follows,

[Pm2.5,Rh,Vis] = visibility(Td,Tw,AQI,Pm)

inputs:
Td = Dry-bulb Temperature (°C)

Tw= Dew-Point Temperature (°C)

Pm=PM2.5 value (g/m3)

AQI=Air Quality Index

Outputs:

Pm25 = PM2.5 Value (g/m3) (Useful if using AQI)

Rh = Relative Humidity (%)

Vis = Visibility (km)

Example:

[Pm25,Rh,vis] = visibility(23,17,-1,6)

PM2.5 = 6

RH: 68.97340750840588

Visibility = 56 km


It should be noted that the AQI is an alternative measure of PM value when PM2.5 is the highest pollutant considered. Please consult Air Quality Index for more information (https://en.wikipedia.org/wiki/Air_quality_index). If you do not want to use AQI, set it to -1. If you choose to use AQI conversion, make sure to set PM=-1. If both are set to -1, there will be an error. 

In time, I would like to use this model to estimate upper altitude visibility. However, this is made to be more complex due to the longer light path to consider (at cruising altitude, this would be >10 km). This means we would have to consider a much larger column density of PM2.5, and then what RH to consider along that longer path? Add refraction issues due to the curvature of the Earth and a density gradients; it is a more complicated problem. 

Reference:
Liu et la., 2013 “Formation and evolution mechanism of regional haze: a case study in the megacity Beijing, China”, Atmos. Chem. Phys., 13, 4501–4514, 2013,www.atmos-chem-phys.net/13/4501/2013/doi:10.5194/acp-13-4501-2013, 

