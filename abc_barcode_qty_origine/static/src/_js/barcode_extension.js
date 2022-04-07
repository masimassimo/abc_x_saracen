odoo.define('stock_barcode_qty_extension', function(require){
    var core = require('web.core');
    var inventory_client_action = require('stock_barcode.inventory_client_action');
    
    alert(core._t('Hello World'));
    
    var custom_inv_c_act = inventory_client_action.extend({
    
    //OVERRIDE
    _makeNewLine: function (params) {
        var virtualId = this._getNewVirtualId();
        var currentPage = this.pages[this.currentPageIndex];
        var newLine = {
            'inventory_id': this.currentState.id,
            'product_id': {
                'id': params.product.id,
                'display_name': params.product.display_name,
                'barcode': params.barcode,
                'tracking': params.product.tracking,
            },
            'product_barcode': params.barcode,
            'display_name': params.product.display_name,
            'product_qty': params.qty_done,
            'move_qty_origin': 10,
            'theoretical_qty': 0,
            'product_uom_id': params.product.uom_id[0],
            'location_id': {
                'id': currentPage.location_id,
                'name': currentPage.location_name,
            },
            'package_id': params.package_id,
            'state': 'confirm',
            'reference': this.name,
            'virtual_id': virtualId,
            'partner_id': params.owner_id,
        };
        return newLine;
    }
    })
    
    
    //alert(core._t('Hello world'));
    
    //return {
        //void
    //}
    
//core.action_registry.add('stock_barcode_qty_extension', custom_inv_c_act);

//return custom_inv_c_act;
})