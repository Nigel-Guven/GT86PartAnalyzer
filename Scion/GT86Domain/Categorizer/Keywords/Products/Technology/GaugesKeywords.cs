using GT86Domain.Fields;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Keywords.Products.Technology
{
    public class GaugesKeywords
    {
        /*
         *
         * Gauges
         *
         */
        public Dictionary<string, List<string>> GetBoostGaugeKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Boost_Gauge, new List<string>() { "Boost", "gauge", "sensor", gauges.Boost_Gauge }}
            };
        }
        public Dictionary<string, List<string>> GetOilPressureGaugeKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Oil_Pressure_Gauge, new List<string>() { "Oil", "pressure", "sensor", "gauge", gauges.Oil_Pressure_Gauge }}
            };
        }
        public Dictionary<string, List<string>> GetOilTemperatureKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Oil_Temperature_Gauge, new List<string>() { "Oil", "temperature", "sensor", "gauge", gauges.Oil_Temperature_Gauge }}
            };
        }
        public Dictionary<string, List<string>> GetSwitchRelocationKitKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Switch_Relocation_Kit, new List<string>() { "switch", "relocation", "kit", gauges.Switch_Relocation_Kit }}
            };
        }
        public Dictionary<string, List<string>> GetGaugeKitKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Gauge_Kit, new List<string>() { "kit", "gauge", "sensor", gauges.Gauge_Kit }}
            };
        }
        public Dictionary<string, List<string>> GetIntakeAirTemperatureKeywords(Gauges gauges)
        {
            return new Dictionary<string, List<string>>()
            {
                { gauges.Intake_Temperature_Gauge, new List<string>() { "intake", "air", "temperature", "sensor", "gauge", gauges.Intake_Temperature_Gauge }}
            };
        }
    }
}
