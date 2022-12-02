select po.name "Muestra",
	po.date_order "FH Muestra",
	co.fechahoracaptura "FH Guia", 
	co.fecha_guia, 
	co.hora_entrada, 
	co.dia_zafra ,
	co.lote_hora ,
	co.turno "Turno 12 Hrs",
	me.codigo_activo "Caja",
	(case WHEN me.codigo_activo = co.caja1 then co.alce1 else co.alce2 end) "EQUIPO CyA" ,
	(case WHEN me.codigo_activo = co.caja1 then co.epl_alce1 else co.epl_alce2 end) "Operador CyA" ,
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
	po.tipo_cane "Tipo Cania",
	po.hdc "FechaHora Corte",
	po.qty_total "Cant. Total",
	po.porc_impureza "_% Impur.",
	pc."name" "Categoria",
	t.description "Nota/Causa",
	t.default_code "Código M.E.",
	l."name" "Nombre M.E.",
	l.product_qty "Peso M.E.",
	l.porc_item "_% M.E.",
	(l.longitud_avg) "_Longitud"
	from "p14_CADASA_2021".public.sample_order_line l
        join "p14_CADASA_2021".public.sample_order po on (l.order_id=po.id)
        join "p14_CADASA_2021".public.res_partner partner on po.partner_id = partner.id
            left join "p14_CADASA_2021".public.product_product p on (l.product_id=p.id)
                left join "p14_CADASA_2021".public.product_template t on (p.product_tmpl_id=t.id)
                	left join "p14_CADASA_2021".public.product_category pc on (pc.id=t.categ_id)
        left join "p14_CADASA_2021".public.uom_uom line_uom on (line_uom.id=l.product_uom)
        left join "p14_CADASA_2021".public.uom_uom product_uom on (product_uom.id=t.uom_id)
        left join "p14_CADASA_2021".public.project_project pp on (pp.id = po.projects_id)
        	left join "p14_CADASA_2021".public.fincas_pma_up fpu on (fpu.id = pp.up)
        left join "p14_CADASA_2021".public.fincas_pma_variedades fpv on (fpv.id = po.variedad)
        left join "p14_CADASA_2021".public.fincas_pma_tiposcortes fpt on (fpt.id = po.tipocorte)
        left join "p14_CADASA_2021".public.purchase_order co on (cast (co.secuencia_guia as VARCHAR ) = po.guia) 
        	left join "p14_CADASA_2021".public.maintenance_equipment me on (me.id=po.caja_muestra)
        order by PO.date_order, l.product_id 