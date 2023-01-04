import logo from '../images/logo.png'
import illustration from "../images/landingillustration.png"
import '../App.css'
import { Link } from 'react-router-dom'
import googlelogo from '../images/googlelogo.png'

const LandingPage = () => {
    return ( 
        
    <div className="w-full h-screen flex flex-row justify-between items-center bg-blue-500 px-[5%] ">  
  
    <div className="flex flex-col space-y-4 pl-[10%]">
            <img src={logo} className="w-[280px] mb-[60px]"  alt="logo" />
            <p className="text-white text-[100%]"> FindIn UN site de soutien scolaire,<br />
            ou vous pouvez déposer vos annonces ,<br />
            chercher l’annonce que vous plait ou le prof <br />
            qui peut vous aider , juste une clique...  </p>
            <img src={illustration} className="w-[450px] mt-[20px]"  alt="" />

    </div>
   
        <div className="flex flex-col items-center  bg-black-600 border-2 border-white h-[80%] w-[400px]">
             <p className=" bg-black-600 m-[1%] text-white "> Veuillez connecter avec votre compte google </p>
            <div className="mt-[30%] flex flex-col justify-center items-center space-y-6 ">
                    <img src={googlelogo} className="w-[50px]" alt="" />
                    <p className="text-white "> with google </p>
                    <Link className=" text-white  py-[10px] px-[80px] bg-blue-600 hover:bg-blue-200  " to=""> Authentification </Link>
            </div> 
        </div>

      </div>
     );
}
 
export default LandingPage;