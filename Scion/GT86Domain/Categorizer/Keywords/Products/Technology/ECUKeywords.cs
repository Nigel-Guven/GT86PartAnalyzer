using GT86Domain.Fields;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Keywords.Products.Technology
{
    public class ECUKeywords
    {
        /*
         *
         * ECU
         *
         */
        public Dictionary<string, List<string>> GetRemappingSoftwareKeywords(ECU ecu)
        {
            return new Dictionary<string, List<string>>()
            {
                { ecu.Remapping_Software, new List<string>() { "Remap", ecu.Remapping_Software }}
            };
        }
        public Dictionary<string, List<string>> GetECUDeviceKeywords(ECU ecu)
        {
            return new Dictionary<string, List<string>>()
            {
                { ecu.ECU_Device, new List<string>() { "ecu", "device", ecu.ECU_Device }}
            };
        }
        public Dictionary<string, List<string>> GetECULicenceKeywords(ECU ecu)
        {
            return new Dictionary<string, List<string>>()
            {
                { ecu.ECU_Licence, new List<string>() { "ecu", "licence", ecu.ECU_Licence }}
            };
        }
        public Dictionary<string, List<string>> GetPedalboxKeywords(ECU ecu)
        {
            return new Dictionary<string, List<string>>()
            {
                { ecu.Pedalbox, new List<string>() { "pedalbox", "dte", "response", ecu.Pedalbox }}
            };
        }
        public string Remapping_Software => "Remapping Software";
        public string ECU_Device => "ECU Device";
        public string ECU_Licence => "ECU Licence";
        public string Pedalbox => "Pedalbox";

        /*
         *
         * Logging Software
         *
         */
        public string OBD_Tool => "OBD Device";

        /*
         *
         * Cabin Devices 
         *
         */
        public string Bluetooth_Device => "Bluetooth Device";
        public string Head_Unit => "Head Unit";
    }
}
