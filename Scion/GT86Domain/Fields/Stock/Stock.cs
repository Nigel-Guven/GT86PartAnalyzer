using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GT86Domain.Stock
{
    public class Stock
    {
        public enum StockClassificationType
        {
            Not_In_Stock = 0,
            Preorder_Only = 1,
            In_Stock = 2,
            Discontinued = 3
        }
    }
}
