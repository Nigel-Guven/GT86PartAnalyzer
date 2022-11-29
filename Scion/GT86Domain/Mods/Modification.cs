using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Mods
{
    public class Modification : BaseStatistics
    {
        public string Name { get; set; }
        public string Brand { get; set; }

        public Modification(string oName, string oBrand, int oScore, double oSpeed, double oHandling, double oAcceleration, double oLaunch, double oBraking) 
            : base (oScore, oSpeed, oHandling, oAcceleration, oLaunch, oBraking)
        {
            Name = oName;
            Brand = oBrand;
            Score = oScore;
            Speed = oSpeed;
            Handling = oHandling;
            Acceleration = oAcceleration;
            Launch = oLaunch;
            Braking = oBraking;
        }
        
    }
}
