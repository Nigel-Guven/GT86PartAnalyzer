using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Mods
{
    public class BaseStatistics
    {
        public int Score { get; set; }
        public double Speed { get; set; }
        public double Handling { get; set; }
        public double Acceleration { get; set; }
        public double Launch { get; set; }
        public double Braking { get; set; }

        public BaseStatistics(int oScore, double oSpeed, double oHandling, double oAcceleration, double oLaunch, double oBraking)
        {
            Score = oScore;
            Speed = oSpeed;
            Handling = oHandling;
            Acceleration = oAcceleration;
            Launch = oLaunch;
            Braking = oBraking;
        }
    }
}
