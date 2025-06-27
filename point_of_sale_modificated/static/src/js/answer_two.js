/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { reactive } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    async addProductToOrder(product) {
        // Validación de precio cero
        if (product.lst_price === 0) {
            window.alert(`⚠️ El producto "${product.display_name}" tiene precio 0.0 y no puede ser añadido.`);
            return;
        }

        // Lógica original
        await reactive(this.pos).addLineToCurrentOrder({ product_id: product }, {});
    },
});
