/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PaymentScreen.prototype, {
  sendDialog() {
    let currentOrder = this.pos.models["pos.order"].getBy(
      "uuid",
      this.props.orderUuid
    );
    let total = this.env.utils.formatCurrency(currentOrder.getTotalDue());

    this.dialog.add(AlertDialog, {
      title: "Informativo",
      body: `El monto total a pagar es: ${total}`,
    });
  },
});
