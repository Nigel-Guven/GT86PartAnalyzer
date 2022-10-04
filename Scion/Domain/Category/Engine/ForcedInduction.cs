﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Category.Engine
{
    public class ForcedInduction
    {
        /*
         * 
         * Turbocharging
         * 
         */
        public string Turbocharger => "Turbocharger";
        public string Turbocharger_Billet => "Turbocharger Billet";
        public string Turbo_Blanket => "Turbo_Blanket";
        public string Breather_System => "Breather System";
        public string Wastegate => "Wastegate";

        /*
         * 
         * Supercharging
         * 
         */
        public string Supercharger => "Supercharger";
        public string Supercharger_Belt => "Supercharger Belt";

        /*
         * 
         * Valves
         * 
         */     
        public string Dump_Valve => "Dump Valve";
        public string Boost_Valve => "Boost Valve";
    }
}
