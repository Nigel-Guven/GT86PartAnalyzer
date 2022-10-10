using GT86Domain.Fields;

namespace GT86Domain.Keywords
{
    public class WheelsKeywords
    {
        /*
         *
         * Alloys
         *
         */
        public Dictionary<string, List<string>> GetAlloyWheelsKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Alloy_Wheel, new List<string>() { "Diameter", "Width", "Wheel", "PCD", "Offset", wheels.Alloy_Wheel }}
            };
        }
        public Dictionary<string, List<string>> GetWheelSpacersKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Wheel_Spacers, new List<string>() { "Spacers", "Hubcentric", "mm", wheels.Wheel_Spacers }}
            };
        }
        public Dictionary<string, List<string>> GetTyrePressureMonitorKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Tyre_Pressure_Monitor, new List<string>() { "Pressure", "Monitor", wheels.Tyre_Pressure_Monitor }}
            };
        }
        public Dictionary<string, List<string>> WheelNutsKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Wheel_Nuts, new List<string>() { "fitment", "m12", wheels.Wheel_Nuts }}
            };
        }

        /*
         *
         * Wheel Assembly
         *
         */
        public Dictionary<string, List<string>> RearWheelBearingKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Rear_Wheel_Bearing, new List<string>() { "Hub Sub Assembly", "Wheel Bearing", "Rear", wheels.Rear_Wheel_Bearing }}
            };
        }
        public Dictionary<string, List<string>> FrontWheelBearingKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Front_Wheel_Bearing, new List<string>() { "Hub Sub Assembly", "Wheel Bearing", "Front", wheels.Front_Wheel_Bearing }}
            };
        }
        public Dictionary<string, List<string>> FrontWheelHubKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Front_Wheel_Hub, new List<string>() { "Hub Sub Assembly", "Wheel Bearing", "Hub", wheels.Front_Wheel_Hub }}
            };
        }
        public Dictionary<string, List<string>> RearWheelHubKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Rear_Wheel_Hub, new List<string>() { "Hub Sub Assembly", "Wheel Bearing", "Hub", wheels.Rear_Wheel_Hub }}
            };
        }
        public Dictionary<string, List<string>> WheelStudsKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Wheel_Studs, new List<string>() { "Wheel Stud", "M12", "65mm long", wheels.Wheel_Studs }}
            };
        }
        public Dictionary<string, List<string>> HubRingsKeywords(Wheels wheels)
        {
            return new Dictionary<string, List<string>>()
            {
                { wheels.Hub_Rings, new List<string>() { "Hub Rings","Hubcentric", "flange", "hub", "ring", wheels.Hub_Rings }}
            };
        }
    }
}