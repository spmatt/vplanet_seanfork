from benchmark import Benchmark, benchmark 
import astropy.units as u 
 
@benchmark( 
   { 
       "log.initial.system.Age": {"value": 3.155760e+13, "unit": u.sec}, 
       "log.initial.system.Time": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.TotAngMom": {"value": 5.653691e+33, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.system.TotEnergy": {"value": -8.955530e+32, "unit": u.Joule}, 
       "log.initial.system.PotEnergy": {"value": -8.957586e+32, "unit": u.Joule}, 
       "log.initial.system.KinEnergy": {"value": 2.055740e+29, "unit": u.Joule}, 
       "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.planet.Mass": {"value": 2.000000, "unit": u.Mearth}, 
       "log.initial.planet.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.initial.planet.RadGyra": {"value": 0.400000}, 
       "log.initial.planet.BodyType": {"value": 0.000000}, 
       "log.initial.planet.Density": {"value": 1.099008e+04, "unit": u.kg / u.m ** 3}, 
       "log.initial.planet.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.HZLimRecVenus": {"value": -1.000000}, 
       "log.initial.planet.HZLimRunaway": {"value": -1.000000}, 
       "log.initial.planet.HZLimMoistGreenhouse": {"value": -1.000000}, 
       "log.initial.planet.HZLimMaxGreenhouse": {"value": -1.000000}, 
       "log.initial.planet.HZLimEarlyMars": {"value": -1.000000}, 
       "log.initial.planet.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.initial.planet.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec}, 
       "log.initial.planet.OrbPeriod": {"value": -1.000000, "unit": u.sec}, 
       "log.initial.planet.SemiMajorAxis": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.initial.planet.SurfWaterMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.planet.EnvelopeMass": {"value": 1.000000, "unit": u.Mearth}, 
       "log.initial.planet.OxygenMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.planet.RGLimit": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.XO": {"value": 0.000000}, 
       "log.initial.planet.EtaO": {"value": 0.000000}, 
       "log.initial.planet.PlanetRadius": {"value": 1.000000, "unit": u.Rearth}, 
       "log.initial.planet.OxygenMantleMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.planet.RadXUV": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.RadSolid": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.PresXUV": {"value": 5.000000}, 
       "log.initial.planet.ScaleHeight": {"value": -1.000000, "unit": u.m}, 
       "log.initial.planet.ThermTemp": {"value": 400.000000, "unit": u.K}, 
       "log.initial.planet.AtmGasConst": {"value": 4124.000000}, 
       "log.initial.planet.PresSurf": {"value": -1.000000, "unit": u.Pa}, 
       "log.initial.planet.DEnvMassDt": {"value": -1.022483e+07, "unit": u.kg / u.sec}, 
       "log.initial.planet.FXUV": {"value": 100.000000, "unit": u.W / u.m ** 2}, 
       "log.initial.planet.AtmXAbsEffH2O": {"value": 0.300000}, 
       "log.initial.planet.RocheRadius": {"value": 2.818540e+301, "unit": u.Rearth}, 
       "log.initial.planet.BondiRadius": {"value": -1.567865e-07, "unit": u.Rearth}, 
       "log.initial.planet.HEscapeRegime": {"value": 3.000000}, 
       "log.initial.planet.RRCriticalFlux": {"value": 483.370798, "unit": u.W / u.m ** 2}, 
       "log.initial.planet.CrossoverMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.planet.WaterEscapeRegime": {"value": 8.000000}, 
       "log.initial.planet.FXUVCRITDRAG": {"value": 1.065443, "unit": u.W / u.m ** 2}, 
       "log.initial.planet.HREFFLUX": {"value": 3.613564e+19, "unit": 1 / u.m ** 2 / u.sec}, 
       "log.initial.planet.XO2": {"value": 0.000000}, 
       "log.initial.planet.XH2O": {"value": 0.000000}, 
       "log.initial.planet.HDiffFlux": {"value": 3.794622e+17, "unit": 1 / u.m ** 2 / u.sec}, 
       "log.initial.planet.HRefODragMod": {"value": 1.000000}, 
       "log.initial.planet.KTide": {"value": 1.000000}, 
       "log.initial.planet.RGDuration": {"value": 1.00000e+06, "unit": u.yr}, 
       "log.final.system.Age": {"value": 6.311520e+13, "unit": u.sec}, 
       "log.final.system.Time": {"value": 3.155760e+13, "unit": u.sec}, 
       "log.final.system.TotAngMom": {"value": 5.653538e+33, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.final.system.TotEnergy": {"value": -8.955046e+32, "unit": u.Joule}, 
       "log.final.system.PotEnergy": {"value": -8.957102e+32, "unit": u.Joule}, 
       "log.final.system.KinEnergy": {"value": 2.055685e+29, "unit": u.Joule}, 
       "log.final.system.DeltaTime": {"value": 3.155760e+13, "unit": u.sec}, 
       "log.final.planet.Mass": {"value": 1.999946, "unit": u.Mearth}, 
       "log.final.planet.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.final.planet.RadGyra": {"value": 0.400000}, 
       "log.final.planet.BodyType": {"value": 0.000000}, 
       "log.final.planet.Density": {"value": 1.098978e+04, "unit": u.kg / u.m ** 3}, 
       "log.final.planet.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.HZLimRecVenus": {"value": -1.000000}, 
       "log.final.planet.HZLimRunaway": {"value": -1.000000}, 
       "log.final.planet.HZLimMoistGreenhouse": {"value": -1.000000}, 
       "log.final.planet.HZLimMaxGreenhouse": {"value": -1.000000}, 
       "log.final.planet.HZLimEarlyMars": {"value": -1.000000}, 
       "log.final.planet.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.final.planet.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec}, 
       "log.final.planet.OrbPeriod": {"value": -1.000000, "unit": u.sec}, 
       "log.final.planet.SemiMajorAxis": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.final.planet.SurfWaterMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.planet.EnvelopeMass": {"value": 0.999946, "unit": u.Mearth}, 
       "log.final.planet.OxygenMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.planet.RGLimit": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.XO": {"value": 0.000000}, 
       "log.final.planet.EtaO": {"value": 0.000000}, 
       "log.final.planet.PlanetRadius": {"value": 1.000000, "unit": u.Rearth}, 
       "log.final.planet.OxygenMantleMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.planet.RadXUV": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.RadSolid": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.PresXUV": {"value": 5.000000}, 
       "log.final.planet.ScaleHeight": {"value": -1.000000, "unit": u.m}, 
       "log.final.planet.ThermTemp": {"value": 400.000000, "unit": u.K}, 
       "log.final.planet.AtmGasConst": {"value": 4124.000000}, 
       "log.final.planet.PresSurf": {"value": -1.000000, "unit": u.Pa}, 
       "log.final.planet.DEnvMassDt": {"value": -1.022497e+07, "unit": u.kg / u.sec}, 
       "log.final.planet.FXUV": {"value": 100.000000, "unit": u.W / u.m ** 2}, 
       "log.final.planet.AtmXAbsEffH2O": {"value": 0.300000}, 
       "log.final.planet.RocheRadius": {"value": 2.818540e+301, "unit": u.Rearth}, 
       "log.final.planet.BondiRadius": {"value": -1.567865e-07, "unit": u.Rearth}, 
       "log.final.planet.HEscapeRegime": {"value": 3.000000}, 
       "log.final.planet.RRCriticalFlux": {"value": 483.344682, "unit": u.W / u.m ** 2}, 
       "log.final.planet.CrossoverMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.planet.WaterEscapeRegime": {"value": 8.000000}, 
       "log.final.planet.FXUVCRITDRAG": {"value": 1.065385, "unit": u.W / u.m ** 2}, 
       "log.final.planet.HREFFLUX": {"value": 3.613662e+19, "unit": 1 / u.m ** 2 / u.sec}, 
       "log.final.planet.XO2": {"value": 0.000000}, 
       "log.final.planet.XH2O": {"value": 0.000000}, 
       "log.final.planet.HDiffFlux": {"value": 3.794519e+17, "unit": 1 / u.m ** 2 / u.sec}, 
       "log.final.planet.HRefODragMod": {"value": 1.000000}, 
       "log.final.planet.KTide": {"value": 1.000000}, 
       "log.final.planet.RGDuration": {"value": 1.00000e+06, "unit": u.yr}, 
   } 
)
class Test_HydELimConstXUVNone(Benchmark): 
   pass 
