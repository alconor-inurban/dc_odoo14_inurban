select po.name "Muestra",
	po.date_order "Fecha Hora",
	partner.name "Proveedor",
	po.state "Estatus",
	po.guia,
	po.tickete,
	po.frente ,
	pp."name" "Nombre Proyecto" ,
	fpu."name" "UP",
	pp.lote,	
	fpv."name" "Variedad",
	fpt."name" "TDCorte",
	po.tipo_cane "Tipo Caña",
	po.hdc "FechaHora Corte",
	po.qty_total "Cant. Total",
	po.porc_impureza "_% Impur.",
	l."name" "Nombre M.E.",
	l.product_qty "Peso M.E.",
	l.porc_item "_% M.E."
	from sample_order_line l
        join sample_order po on (l.order_id=po.id)
        join res_partner partner on po.partner_id = partner.id
            left join product_product p on (l.product_id=p.id)
                left join product_template t on (p.product_tmpl_id=t.id)
        left join uom_uom line_uom on (line_uom.id=l.product_uom)
        left join uom_uom product_uom on (product_uom.id=t.uom_id)
        left join project_project pp on (pp.id = po.projects_id)
        	left join fincas_pma_up fpu on (fpu.id = pp.up)
        left join fincas_pma_variedades fpv on (fpv.id = po.variedad)
        left join fincas_pma_tiposcortes fpt on (fpt.id = po.tipocorte)
     order by po.date_order , l."name" 
