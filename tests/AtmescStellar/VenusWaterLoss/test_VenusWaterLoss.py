import astropy.units as u
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 1.577880e15, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 1.857267e41,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -2.543479e41, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -2.543481e41, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 2.027568e35, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.sun.Mass": {"value": 1.988416e30, "unit": u.kg},
        "log.initial.sun.Radius": {"value": 97.600120, "unit": u.Rearth},
        "log.initial.sun.RadGyra": {"value": 0.299270},
        "log.initial.sun.RotAngMom": {
            "value": 1.672864e41,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.sun.RotVel": {"value": 1508.990649, "unit": u.m / u.sec},
        "log.initial.sun.BodyType": {"value": 0.000000},
        "log.initial.sun.RotRate": {"value": 2.424068e-06, "unit": 1 / u.sec},
        "log.initial.sun.RotPer": {"value": 2.592000e06, "unit": u.sec},
        "log.initial.sun.Density": {"value": 1967.857326, "unit": u.kg / u.m**3},
        "log.initial.sun.HZLimitDryRunaway": {"value": 1.117482e11, "unit": u.m},
        "log.initial.sun.HZLimRecVenus": {"value": 9.298839e10, "unit": u.m},
        "log.initial.sun.HZLimRunaway": {"value": 1.219900e11, "unit": u.m},
        "log.initial.sun.HZLimMoistGreenhouse": {"value": 1.230381e11, "unit": u.m},
        "log.initial.sun.HZLimMaxGreenhouse": {"value": 2.108277e11, "unit": u.m},
        "log.initial.sun.HZLimEarlyMars": {"value": 2.300210e11, "unit": u.m},
        "log.initial.sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec**3},
        "log.initial.sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.sun.LXUVTot": {"value": 2.604948e23, "unit": u.kg / u.sec**3},
        "log.initial.sun.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.sun.LostAngMom": {
            "value": 5.562685e-309,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.sun.Luminosity": {"value": 0.677313, "unit": u.LSUN},
        "log.initial.sun.LXUVStellar": {"value": 0.000677, "unit": u.LSUN},
        "log.initial.sun.Temperature": {"value": 5536.633657, "unit": u.K},
        "log.initial.sun.LXUVFrac": {"value": 0.001000},
        "log.initial.sun.RossbyNumber": {"value": 1.821125},
        "log.initial.sun.DRotPerDtStellar": {"value": 1.168600e-10},
        "log.initial.venus.Mass": {"value": 4.867332e24, "unit": u.kg},
        "log.initial.venus.Radius": {"value": 6.058557e06, "unit": u.m},
        "log.initial.venus.RadGyra": {"value": 0.500000},
        "log.initial.venus.BodyType": {"value": 0.000000},
        "log.initial.venus.Density": {"value": 5225.100994, "unit": u.kg / u.m**3},
        "log.initial.venus.HZLimitDryRunaway": {"value": 1.117508e11, "unit": u.m},
        "log.initial.venus.HZLimRecVenus": {"value": 9.298839e10, "unit": u.m},
        "log.initial.venus.HZLimRunaway": {"value": 1.219900e11, "unit": u.m},
        "log.initial.venus.HZLimMoistGreenhouse": {"value": 1.230381e11, "unit": u.m},
        "log.initial.venus.HZLimMaxGreenhouse": {"value": 2.108277e11, "unit": u.m},
        "log.initial.venus.HZLimEarlyMars": {"value": 2.300210e11, "unit": u.m},
        "log.initial.venus.Instellation": {
            "value": 1772.032378,
            "unit": u.kg / u.sec**3,
        },
        "log.initial.venus.MeanMotion": {"value": 3.238626e-07, "unit": 1 / u.sec},
        "log.initial.venus.OrbPeriod": {"value": 1.940077e07, "unit": u.sec},
        "log.initial.venus.SemiMajorAxis": {"value": 1.081593e11, "unit": u.m},
        "log.initial.venus.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec**3},
        "log.initial.venus.SurfWaterMass": {"value": 3.000000, "unit": u.TO},
        "log.initial.venus.EnvelopeMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.venus.OxygenMass": {"value": 0.000000, "unit": u.kg},
        "log.initial.venus.RGLimit": {"value": 0.797432, "unit": u.au},
        "log.initial.venus.XO": {"value": 0.333333},
        "log.initial.venus.EtaO": {"value": 0.158045},
        "log.initial.venus.PlanetRadius": {"value": 6.058557e06, "unit": u.m},
        "log.initial.venus.OxygenMantleMass": {"value": 0.000000, "unit": u.bar},
        "log.initial.venus.RadXUV": {"value": -1.000000, "unit": u.m},
        "log.initial.venus.RadSolid": {"value": -1.000000, "unit": u.m},
        "log.initial.venus.PresXUV": {"value": 5.000000},
        "log.initial.venus.ScaleHeight": {"value": -1.000000, "unit": u.m},
        "log.initial.venus.ThermTemp": {"value": 400.000000, "unit": u.K},
        "log.initial.venus.AtmGasConst": {"value": 4124.000000},
        "log.initial.venus.PresSurf": {"value": -1.000000, "unit": u.Pa},
        "log.initial.venus.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec},
        "log.initial.venus.FXUV": {"value": 1.772032, "unit": u.W / u.m**2},
        "log.initial.venus.AtmXAbsEffH2O": {"value": 0.061199},
        "log.initial.venus.RocheRadius": {"value": 1.010690e09, "unit": u.m},
        "log.initial.venus.BondiRadius": {"value": 1.264628e07, "unit": u.m},
        "log.initial.venus.HEscapeRegime": {"value": 8.000000},
        "log.initial.venus.RRCriticalFlux": {
            "value": 40.876539,
            "unit": u.W / u.m**2,
        },
        "log.initial.venus.CrossoverMass": {"value": 3.124418e-26, "unit": u.kg},
        "log.initial.venus.WaterEscapeRegime": {"value": 3.000000},
        "log.initial.venus.FXUVCRITDRAG": {"value": 0.674582, "unit": u.W / u.m**2},
        "log.initial.venus.HREFFLUX": {
            "value": 3.072602e17,
            "unit": 1 / u.m**2 / u.sec,
        },
        "log.initial.venus.XO2": {"value": 0.000000},
        "log.initial.venus.XH2O": {"value": 1.000000},
        "log.initial.venus.HDiffFlux": {
            "value": 1.142481e17,
            "unit": 1 / u.m**2 / u.sec,
        },
        "log.initial.venus.HRefODragMod": {"value": 0.441625},
        "log.initial.venus.KTide": {"value": 0.991008},
        "log.initial.venus.RGDuration": {"value": 0.00000e00, "unit": u.yr},
        "log.final.system.Age": {"value": 4.733640e15, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.Time": {"value": 3.155760e15, "unit": u.sec, "rtol": 1e-4},
        "log.final.system.TotAngMom": {
            "value": 1.844368e41,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.system.TotEnergy": {
            "value": -2.545081e41,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.PotEnergy": {
            "value": -2.513263e41,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.system.KinEnergy": {
            "value": 1.923109e35,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.sun.Mass": {"value": 1.988416e30, "unit": u.kg, "rtol": 1e-4},
        "log.final.sun.Radius": {"value": 98.773624, "unit": u.Rearth, "rtol": 1e-4},
        "log.final.sun.RadGyra": {"value": 0.296157, "rtol": 1e-4},
        "log.final.sun.RotAngMom": {
            "value": 1.631641e41,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.sun.RotVel": {
            "value": 1485.051471,
            "unit": u.m / u.sec,
            "rtol": 1e-4,
        },
        "log.final.sun.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.sun.RotRate": {
            "value": 2.357269e-06,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.sun.RotPer": {"value": 2.665451e06, "unit": u.sec, "rtol": 1e-4},
        "log.final.sun.Density": {
            "value": 1898.548508,
            "unit": u.kg / u.m**3,
            "rtol": 1e-4,
        },
        "log.final.sun.HZLimitDryRunaway": {
            "value": 1.138057e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.HZLimRecVenus": {
            "value": 9.461946e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.HZLimRunaway": {"value": 1.240819e11, "unit": u.m, "rtol": 1e-4},
        "log.final.sun.HZLimMoistGreenhouse": {
            "value": 1.251962e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.HZLimMaxGreenhouse": {
            "value": 2.143180e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.HZLimEarlyMars": {
            "value": 2.338299e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.sun.CriticalSemiMajorAxis": {
            "value": -1.000000,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.sun.LXUVTot": {
            "value": 1.640792e23,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.sun.LostEnergy": {
            "value": -3.182033e39,
            "unit": u.Joule,
            "rtol": 1e-4,
        },
        "log.final.sun.LostAngMom": {
            "value": 2.832349e39,
            "unit": (u.kg * u.m**2) / u.sec,
            "rtol": 1e-4,
        },
        "log.final.sun.Luminosity": {"value": 0.702484, "unit": u.LSUN, "rtol": 1e-4},
        "log.final.sun.LXUVStellar": {"value": 0.000427, "unit": u.LSUN, "rtol": 1e-4},
        "log.final.sun.Temperature": {"value": 5557.811473, "unit": u.K, "rtol": 1e-4},
        "log.final.sun.LXUVFrac": {"value": 0.000607, "rtol": 1e-4},
        "log.final.sun.RossbyNumber": {"value": 1.908411, "rtol": 1e-4},
        "log.final.sun.DRotPerDtStellar": {"value": 2.496897e-12, "rtol": 1e-4},
        "log.final.venus.Mass": {"value": 4.867332e24, "unit": u.kg, "rtol": 1e-4},
        "log.final.venus.Radius": {"value": 6.058557e06, "unit": u.m, "rtol": 1e-4},
        "log.final.venus.RadGyra": {"value": 0.500000, "rtol": 1e-4},
        "log.final.venus.BodyType": {"value": 0.000000, "rtol": 1e-4},
        "log.final.venus.Density": {
            "value": 5225.100994,
            "unit": u.kg / u.m**3,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimitDryRunaway": {
            "value": 1.138083e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimRecVenus": {
            "value": 9.461946e10,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimRunaway": {
            "value": 1.240819e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimMoistGreenhouse": {
            "value": 1.251962e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimMaxGreenhouse": {
            "value": 2.143180e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HZLimEarlyMars": {
            "value": 2.338299e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.Instellation": {
            "value": 1837.885093,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.venus.MeanMotion": {
            "value": 3.238626e-07,
            "unit": 1 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.venus.OrbPeriod": {
            "value": 1.940077e07,
            "unit": u.sec,
            "rtol": 1e-4,
        },
        "log.final.venus.SemiMajorAxis": {
            "value": 1.081593e11,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.LXUVTot": {
            "value": -1.000000,
            "unit": u.kg / u.sec**3,
            "rtol": 1e-4,
        },
        "log.final.venus.SurfWaterMass": {
            "value": 0.915086,
            "unit": u.TO,
            "rtol": 1e-4,
        },
        "log.final.venus.EnvelopeMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.venus.OxygenMass": {"value": 0.000000, "unit": u.kg, "rtol": 1e-4},
        "log.final.venus.RGLimit": {"value": 0.811114, "unit": u.au, "rtol": 1e-4},
        "log.final.venus.XO": {"value": 0.333333, "rtol": 1e-4},
        "log.final.venus.EtaO": {"value": 0.093075, "rtol": 1e-4},
        "log.final.venus.PlanetRadius": {
            "value": 6.058557e06,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.OxygenMantleMass": {
            "value": 423.885973,
            "unit": u.bar,
            "rtol": 1e-4,
        },
        "log.final.venus.RadXUV": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.venus.RadSolid": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.venus.PresXUV": {"value": 5.000000, "rtol": 1e-4},
        "log.final.venus.ScaleHeight": {"value": -1.000000, "unit": u.m, "rtol": 1e-4},
        "log.final.venus.ThermTemp": {"value": 400.000000, "unit": u.K, "rtol": 1e-4},
        "log.final.venus.AtmGasConst": {"value": 4124.000000, "rtol": 1e-4},
        "log.final.venus.PresSurf": {"value": -1.000000, "unit": u.Pa, "rtol": 1e-4},
        "log.final.venus.DEnvMassDt": {
            "value": 0.000000,
            "unit": u.kg / u.sec,
            "rtol": 1e-4,
        },
        "log.final.venus.FXUV": {
            "value": 1.116159,
            "unit": u.W / u.m**2,
            "rtol": 1e-4,
        },
        "log.final.venus.AtmXAbsEffH2O": {"value": 0.069496, "rtol": 1e-4},
        "log.final.venus.RocheRadius": {
            "value": 1.010690e09,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.BondiRadius": {
            "value": 1.252303e07,
            "unit": u.m,
            "rtol": 1e-4,
        },
        "log.final.venus.HEscapeRegime": {"value": 8.000000, "rtol": 1e-4},
        "log.final.venus.RRCriticalFlux": {
            "value": 40.876539,
            "unit": u.W / u.m**2,
            "rtol": 1e-4,
        },
        "log.final.venus.CrossoverMass": {
            "value": 2.912488e-26,
            "unit": u.kg,
            "rtol": 1e-4,
        },
        "log.final.venus.WaterEscapeRegime": {"value": 3.000000, "rtol": 1e-4},
        "log.final.venus.FXUVCRITDRAG": {
            "value": 0.594047,
            "unit": u.W / u.m**2,
            "rtol": 1e-4,
        },
        "log.final.venus.HREFFLUX": {
            "value": 2.197731e17,
            "unit": 1 / u.m**2 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.venus.XO2": {"value": 0.000000, "rtol": 1e-4},
        "log.final.venus.XH2O": {"value": 1.000000, "rtol": 1e-4},
        "log.final.venus.HDiffFlux": {
            "value": 1.142481e17,
            "unit": 1 / u.m**2 / u.sec,
            "rtol": 1e-4,
        },
        "log.final.venus.HRefODragMod": {"value": 0.573196, "rtol": 1e-4},
        "log.final.venus.KTide": {"value": 0.991008, "rtol": 1e-4},
        "log.final.venus.RGDuration": {"value": 0.00000e00, "unit": u.yr, "rtol": 1e-4},
    }
)
class Test_VenusWaterLoss(Benchmark):
    pass
