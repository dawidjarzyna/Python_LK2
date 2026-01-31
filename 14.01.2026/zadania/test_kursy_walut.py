from kursy_walut import pobierz_cene_euro

def test_pobierania_kursu_euro_z_mocka(mocker):
    falszywe_dane_od_nbp = {
        'rates': [
            {'mid': 4.99}
        ]
    }

    # 2. Tworzymy fałszywą odpowiedź (Mock)
    mock_response = mocker.Mock()
    mock_response.json.return_value = falszywe_dane_od_nbp

    mocker.patch("kursy_walut.requests.get", return_value=mock_response)

    wynik = pobierz_cene_euro()

    assert wynik == 4.99