using GT86Domain.Fields;

namespace GT86Domain.Mods
{
    public class CarStatistics : BaseStatistics
    {
        public char Rank { get; set; }

        public CarStatistics(
            char oRank, 
            int oScore, 
            double oSpeed, 
            double oHandling, 
            double oAcceleration, 
            double oLaunch, 
            double oBraking) : base(oScore, oSpeed, oHandling, oAcceleration, oLaunch, oBraking)
        {
            this.Rank = oRank;
            Score = oScore;
            Speed = oSpeed;
            Handling = oHandling;
            Acceleration = oAcceleration;
            Launch = oLaunch;
            Braking = oBraking;
        }

        CarStatistics stockCarStatistics = new CarStatistics('C', 579, 5.5, 5.2, 4.2, 3.6, 3.2);

        public CarStatistics GetStatisticsForGT86(
            Manufacturer manufacturer,
            AirIntake airIntake,
            Wheels wheels,
            BodyKit bodyKit, 
            Strengthening strengthening,
            EngineDecoration engineDecoration,
            Struts struts)
        {
            List<Modification> listOfModifications = new List<Modification>
            {
                new Modification(engineDecoration.Brake_Cylinder_Brace, manufacturer.Beatrush, 2, 0.0, 0.2, 0.1, 0.1, 0.2),
                new Modification(strengthening.Rear_Strut_Brace, manufacturer.Hardrace, 1, 0.0, 0.1, 0.0, 0.0, 0.1),
                new Modification(struts.Coilover_Kit, manufacturer.Tein, 1, 0.0, 0.2, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Wind_Deflectors, manufacturer.Hic, 1, 0.1, 0.1, 0.0, 0.0, 0.0),
                new Modification(wheels.Alloy_Wheels, manufacturer.Japan_Racing, 2, 0.0, 0.0, 0.0, 0.0, 0.0),
                new Modification(strengthening.Front_Strut_Brace, manufacturer.Blitz, 1, 0.0, 0.1, 0.0, 0.0, 0.1),
                new Modification(airIntake.Air_Intake_Kit, manufacturer.SK_Import, 9, 0.1, 0.0, 0.1, 0.2, 0.0),
                new Modification(wheels.Tyres, manufacturer.Continental, 22, 0.0, 0.1, 0.1, 0.0, 0.2),
                new Modification(bodyKit.Roof_Spoiler, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Rear_Brake_Kit, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Brake_Hoses, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Sandwich_Plate, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Oil_Temperature_Gauge, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0),
                new Modification(bodyKit.Oil_Pressure_Gauge, manufacturer.SK_Import, 2, 0.0, 0.1, 0.0, 0.0, 0.0)

            };

            var totalScore = 0;
            var totalSpeed = 0.0;
            var totalHandling = 0.0;
            var totalAcceleration = 0.0;
            var totalLaunch = 0.0;
            var totalBraking = 0.0;


            foreach ( Modification mod in listOfModifications) 
            {
                totalScore += mod.Score;
                totalSpeed += mod.Speed;
                totalHandling += mod.Handling;
                totalAcceleration += mod.Acceleration;
                totalLaunch += mod.Launch;
                totalBraking += mod.Braking;

            }

            return new CarStatistics(GetRank(totalScore), totalScore, totalSpeed, totalHandling, totalAcceleration, totalLaunch, totalBraking);
        }

        public static char GetRank(int score)
        {
            return score switch
            {
                > 999 => 'X',
                > 900 => 'S',
                > 800 => 'S',
                > 700 => 'A',
                > 600 => 'B',
                > 500 => 'C',
                _ => 'D',
            };
        }
    }
}
