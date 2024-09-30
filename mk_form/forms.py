from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, HTML, Submit
from crispy_bootstrap5.bootstrap5 import BS5Accordion

from mk_form.models import Data, Player, GameTypeCategory


# TODO: Use forms.Form instead, no 'fields = "__all__"'
class DataModelForm(forms.ModelForm):

    player_first = forms.ChoiceField(initial="None")
    player_second = forms.ChoiceField(initial="None")
    player_third = forms.ChoiceField(initial="None")
    player_fourth = forms.ChoiceField(initial="None")

    def clean(self):
        cleaned_data = super().clean()
        player_first = cleaned_data.get("player_first")
        player_second = cleaned_data.get("player_second")
        player_third = cleaned_data.get("player_third")
        player_fourth = cleaned_data.get("player_fourth")

        game_type = cleaned_data.get("game_type")

        # Two Player Games
        # 2P: Player First or Second can not be "None"
        if (game_type == GameTypeCategory.TWO) & (
            (player_first == "None") | (player_second == "None")
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.TWO}, Player First and/or Second can not be 'None'."
            )

            self.add_error("player_first", msg)
            self.add_error("player_second", msg)

        # 2P: Player First can not equal Player Second
        if (game_type == GameTypeCategory.TWO) & (player_first == player_second):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.TWO}, Player First can not be equal to Player Second."
            )

            self.add_error("game_type", msg)
            self.add_error("player_first", msg)
            self.add_error("player_second", msg)

        # 2P: Player Third and Fourth must be 'None'
        if (game_type == GameTypeCategory.TWO) & (
            (player_third != "None") | (player_fourth != "None")
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.TWO}, Player Third and Fourth must be 'None'."
            )

            self.add_error("game_type", msg)
            self.add_error("player_third", msg)
            self.add_error("player_fourth", msg)

        # 3 Player Games
        # 3P: Player First, Second or Third can not be "None"
        if (game_type == GameTypeCategory.THREE) & (
            (player_first == "None")
            | (player_second == "None")
            | (player_third == "None")
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.THREE}, Player First, Second and/or Third can not be 'None'."
            )

            self.add_error("player_first", msg)
            self.add_error("player_second", msg)
            self.add_error("player_third", msg)

        # 3P: Players must be unique
        if (game_type == GameTypeCategory.THREE) & (
            (player_first == player_second)
            | (player_second == player_third)
            | (player_third == player_first)
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.THREE}, Player First, Second, and Third must be unique."
            )

            self.add_error("game_type", msg)
            self.add_error("player_first", msg)
            self.add_error("player_second", msg)
            self.add_error("player_third", msg)

        # 3P: Player Third and Fourth must be 'None'
        if (game_type == GameTypeCategory.THREE) & (player_fourth != "None"):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.THREE}, Player Fourth must be 'None'."
            )

            self.add_error("game_type", msg)
            self.add_error("player_fourth", msg)

        # 4 Player Games
        # 4P: Player First, Second or Third can not be "None"
        if (game_type == GameTypeCategory.FOUR) & (
            (player_first == "None")
            | (player_second == "None")
            | (player_third == "None")
            | (player_fourth == "None")
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.FOUR}, Player First, Second and/or Third can not be 'None'."
            )

            self.add_error("player_first", msg)
            self.add_error("player_second", msg)
            self.add_error("player_third", msg)
            self.add_error("player_fourth", msg)

        # 4P: Players must be unique
        if (game_type == GameTypeCategory.FOUR) & (
            (player_first == player_second)
            | (player_second == player_third)
            | (player_third == player_first)
        ):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.FOUR}, Player First, Second, Third and Fourth must be unique."
            )

            self.add_error("game_type", msg)
            self.add_error("player_first", msg)
            self.add_error("player_second", msg)
            self.add_error("player_third", msg)
            self.add_error("player_fourth", msg)

    def __init__(self, *args, **kwargs):
        super(DataModelForm, self).__init__(*args, **kwargs)

        choices = Player.objects.values_list("name", flat=True)
        self.fields["player_first"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_second"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_third"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_fourth"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]

        # Crispy Forms
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"

        self.helper.layout = Layout(
            Div(
                HTML("<br>"),
                Div(
                    Row(HTML("<h4>General</h4>")),
                    Row(
                        Column("game_type", css_class="col me-auto"),
                        Column("map_choice", css_class="col me-auto"),
                        css_class="align-items-end justify-content-center",
                    ),
                    css_class="container",
                ),
                HTML("<br>"),
                Div(
                    Row(HTML("<h4>Players</h4>")),
                    Row(
                        Column("player_first", css_class="col me-auto"),
                        Column("player_second", css_class="col me-auto"),
                        Column("player_third", css_class="col me-auto"),
                        Column("player_fourth", css_class="col me-auto"),
                        css_class="align-items-end justify-content-center",
                    ),
                    css_class="container",
                ),
                css_class="form-group",
            ),
            HTML("<br>"),
            Div(
                HTML(
                    "<a href='{% url 'data_list'%}' class='btn btn-secondary'>Cancel</a>"
                ),
                Submit("submit", "Submit", css_class="col"),
                css_class="align-items-end justify-content-start",
            ),
        )

    class Meta:
        model = Data
        fields = [
            "game_type",
            "map_choice",
            "player_first",
            "player_second",
            "player_third",
            "player_fourth",
        ]
