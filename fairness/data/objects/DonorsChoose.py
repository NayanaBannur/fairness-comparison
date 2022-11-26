from fairness.data.objects.Data import Data


class DonorsChoose(Data):
    def __init__(self):
        Data.__init__(self)
        self.dataset_name = 'donors_choose'
        self.class_attr = 'unfunded'
        self.positive_class_val = True
        self.sensitive_attrs = ['poverty_level']
        self.privileged_class_names = ['low poverty']
        self.categorical_features = ['school_metro', 'resource_type', 'primary_focus_area', 'grade_level']
        self.features_to_keep = ['school_metro', 'poverty_level', 'resource_type', 'primary_focus_area',
                                 'grade_level', 'school_charter', 'school_magnet', 'school_year_round',
                                 'teacher_teach_for_america', 'teacher_ny_teaching_fellow',
                                 'eligible_double_your_impact_match', 'amount_requested',
                                 'num_item_types', 'total_num_items', 'avg_price_items',
                                 'title_word_count', 'short_des_word_count', 'need_stmt_word_count',
                                 'essay_word_count', 'school_hist_unfunded_rate', 'unfunded']
        self.missing_val_indicators = []
        self.split_ix = 110536

    def handle_missing_data(self, dataframe):
        return dataframe.fillna('Missing')
