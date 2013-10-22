# SSC开奖计算逻辑
## p_do_calc

	-- sub_draws.status 状态:0:等待,1:开盘,2:关盘;3:计算中;4:计算结束
	IF sub_draws.status IN [NULL,1,2]
		ROLLBACK AND EXIT
	ENDIF;
	
	-- draws_result.status 状态:0:尚未设置号码,1:已经设置号码,2: 5个号码全部设置 3：已开奖计算
	IF draws_result.status IN [NULL,1,2]
		ROLLBACK AND EXIT
	ENDIF;
	
	IF draws_result.status = 2
		UPDATE draws_result.status=4
		
		-- 复制注单至临时表
		ret=CALL p_dump_order_to_tmp()
		IF ret<=0
			ROLLBACK AND EXIT
		ENDIF
		
		-- 复制rpt小期数据至rpt_*，复制完成删除小期数据
		ret=CALL p_move_rpt_curr()
		
	ELSEIF draws_result.status = 3
		
	ENDIF;
	
	
## p_dump_order_to_tmp

	IF _order_id != ''
		CREATE TEMPORARY TABLE `order_curr`
		CREATE TEMPORARY TABLE  `short_covering_user`
		CREATE TEMPORARY TABLE `short_covering_corp`
		CREATE TEMPORARY TABLE `order_rpt_calc`
	ENDIF;
	
	-- 为1时取当期注单表，0则取历史表
	IF _source = 1
		-- 为避免入参日期与order_time不匹配，加此判断
        SELECT tmp.order_time INTO @order_date FROM (
        	SELECT DATE(order_time) AS order_time FROM order_curr WHERE sub_draws_name=@sub_draws_name ORDER BY id ASC LIMIT 1
	        UNION ALL
    	    SELECT DATE(order_time) AS order_time FROM short_covering_corp WHERE sub_draws_name=@sub_draws_name ORDER BY id ASC LIMIT 1
        ) AS tmp LIMIT 1;
        -- 报表结算时注单ID为空，不带order_id条件(建表语句冗余，不用动态SQL是基于性能的考虑)
        IF _order_id = ''
        	
        ENDIF;
        
        
        
        
        
        