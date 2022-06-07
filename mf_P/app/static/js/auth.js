let params = {};
    window.location.search.slice(1).split('&').forEach(elm => {
      if (elm === '') return;
      let spl = elm.split('=');
      const d = decodeURIComponent;
      params[d(spl[0])] = (spl.length >= 2 ? d(spl[1]) : true);
    });
    const c = params['code'];
    console.log(params['code'])

    if (c){
      let requestOptions = {
        method: 'POST',
        redirect: 'follow'
      };
      // location.reload()
      fetch("https://sso.egov.uz/sso/oauth/Authorization.do?grant_type=one_authorization_code&client_id=msfoLCfee.mf.uz&client_secret=j8GIpJRNoUgq1BEM2HCiuAhb&redirect_uri=http%3A%2F%2Flocalhost:8000/ariza&code=" + c, requestOptions)
          .then(response => response.json())
          .then(result => {
                if (result['access_token']) {
                    console.log("SENT!")
                  const authToken = result['access_token'];
                  localStorage.setItem('auth2', authToken);
                }
                console.log("DONT SENT!")

                //window.history.back();
                // window.history.forward();
              }
          )
          .catch(error => console.log('error', error));
    };



    let sur_name = document.getElementById('sur_name');
    let full_name = document.getElementById('full_name');
    let fio = document.getElementById('fio');
    let mid_name = document.getElementById('mid_name');
    let birth_date = document.getElementById('birth_date');
    let mob_phone_no = document.getElementById('mob_phone_no');
    let pin = document.getElementById('pin');
    let email = document.getElementById('email');
    let issue_date = document.getElementById('issue_date');
    let expr_date = document.getElementById('expr_date');
    let pport_no = document.getElementById('pport_no');
    let pport_issue_place = document.getElementById('pport_issue_place');
    let ctzn = document.getElementById('ctzn');

    let per_adr = document.getElementById('per_adr');


    const logOut = () => {
      let requestOptions = {
        method: 'POST',
        redirect: 'follow'
      };
      fetch("https://sso.egov.uz/sso/oauth/Authorization.do?grant_type=one_log_out&client_id=msfoLCfee.mf.uz&client_secret=j8GIpJRNoUgq1BEM2HCiuAhb&access_token="+ localStorage.getItem('auth2') + "&scope=localhost_mf_uz", requestOptions)
      .then(() => {
        localStorage.removeItem('auth2');
        window.location.href = "/";
        console.log("SUMbUL SOCH");
      })
      .catch((error) => console.log(error));
    };


    const userInfo = (user) => {
       //console.log('resss', user);
        full_name.innerText = user.sur_name +' '+ user.first_name +' '+ user.mid_name;
        fio.innerText = user.sur_name +' '+ user.first_name +' '+ user.mid_name;
        birth_date.innerText = user.birth_date;
        mob_phone_no.innerText = user.mob_phone_no;
        pin.innerText = user.pin;
        email.innerText = user.email;
        issue_date.innerText = user._pport_issue_date;
        expr_date.innerText = user._pport_expr_date;
        pport_no.innerText = user.pport_no;
        pport_issue_place.innerText = user.pport_issue_place;
        ctzn.innerText = user.ctzn;
        per_adr.innerText = user.per_adr;
    }

     const getUser = () => {
        let requestOptions = {
            method: 'POST',
            redirect: 'follow'
          };
     fetch('https://sso.egov.uz/sso/oauth/Authorization.do?grant_type=one_access_token_identify&client_id=msfoLCfee.mf.uz&client_secret=j8GIpJRNoUgq1BEM2HCiuAhb&access_token='+ localStorage.getItem('auth2') +'&scope=localhost_mf_uz', requestOptions)
     .then(response => response.json())
     .then(result => {
            userInfo(result);
         console.log('result:',result)
         }
     )
     .catch(error => console.log('error', error));
    };

    getUser();
    // // hemis token //
    // const headers = {'Authorization': 'Basic Y2xpZW50OnNlY3JldA=='};
    // const formData = new FormData();
    //       formData.append("grant_type", "password");
    //       formData.append("username", "moliya");
    //       formData.append("password", "isYAa2R6z9dP9YV");
    //
    // async function hemisToken(pnfl) {
    //   try {
    //     const response = await fetch('http://ministry.hemis.uz/app/rest/v2/oauth/token', {
    //       method: 'POST',
    //       headers: headers,
    //       body: formData,
    //       redirect: 'follow'
    //     });
    //     const json = await response.json();
    //           localStorage.setItem('_hemisToken', json.access_token);
    //     // hemis student //
    //       globalFetch(`http://ministry.hemis.uz/app/rest/v2/services/student/get?pinfl=${pnfl}`, {
    //       method: 'GET',
    //       headers: {'Authorization': `Bearer ${localStorage.getItem('_hemisToken')}`},
    //       redirect: 'follow'
    //     }).then(json => {
    //       console.log('json', json);
    //     })
    //   }
    //      catch(error) {
    //         console.log('error', error);
    //         return null;
    //       }
    // };