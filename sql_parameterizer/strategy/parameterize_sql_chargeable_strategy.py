from sql_parameterizer.strategy.abstract_parameterize_sql_strategy import ParameterizeSqlStrategy
from string import Template


class ParameterizeSqlChargeableStrategy:

    @staticmethod
    def generate_query_string(partner_id, product, partner_purchased_plan_id, plan, usage):
        template = "INSERT INTO chargeable VALUES ($partner_id, $product, $partner_purchased_plan_id,$plan, $usage)"

        result = Template(template).substitute(
            partner_id=partner_id,
            product=product,
            partner_purchased_plan_id=partner_purchased_plan_id,
            plan=plan,
            usage=usage
        )

        return result

    def parameterize_df_to_sql(self, data_ref):
        print("Recieved DF")
        print(data_ref.head())
        print(data_ref.columns)

        data_ref["chargeable_sql_insert"] = data_ref.apply(lambda row: self.generate_query_string(
            row["PartnerID"], row["PartNumber_mapped"], row["accountGuid"], row["plan"], row["itemCount"]
        ), axis=1)