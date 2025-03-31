
import { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { LogIn, LogOut, Menu, X } from "lucide-react";
import { useAuth } from "@/microservices/user/frontend/hooks/use-auth";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { isAuthenticated, login, logout } = useAuth();

  return (
    <nav className="bg-white shadow-sm py-4 px-6">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold text-teal-600">ShareARider</Link>
        
        {/* Desktop navigation */}
        <div className="hidden md:flex items-center gap-6">
          <Link to="/" className="text-gray-700 hover:text-teal-600 transition-colors">Home</Link>
          <Link to="/how-it-works" className="text-gray-700 hover:text-teal-600 transition-colors">How It Works</Link>
          {isAuthenticated ? (
            <>
              <Link to="/dashboard" className="text-gray-700 hover:text-teal-600 transition-colors">Dashboard</Link>
              <Button 
                variant="outline"
                onClick={logout}
                className="flex items-center gap-2"
              >
                <LogOut size={16} />
                Sign Out
              </Button>
            </>
          ) : (
            <Button
              onClick={login}
              className="flex items-center gap-2"
            >
              <LogIn size={16} />
              Sign In
            </Button>
          )}
        </div>

        {/* Mobile menu button */}
        <button 
          className="md:hidden text-gray-700"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile navigation */}
      {isMenuOpen && (
        <div className="md:hidden absolute top-16 left-0 right-0 bg-white shadow-md z-50 py-4">
          <div className="container mx-auto flex flex-col space-y-4 px-6">
            <Link 
              to="/"
              className="text-gray-700 hover:text-teal-600 transition-colors py-2"
              onClick={() => setIsMenuOpen(false)}
            >
              Home
            </Link>
            <Link 
              to="/how-it-works"
              className="text-gray-700 hover:text-teal-600 transition-colors py-2"
              onClick={() => setIsMenuOpen(false)}
            >
              How It Works
            </Link>
            {isAuthenticated ? (
              <>
                <Link 
                  to="/dashboard"
                  className="text-gray-700 hover:text-teal-600 transition-colors py-2"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Dashboard
                </Link>
                <Button 
                  variant="outline"
                  onClick={() => {
                    logout();
                    setIsMenuOpen(false);
                  }}
                  className="flex items-center justify-center gap-2 w-full"
                >
                  <LogOut size={16} />
                  Sign Out
                </Button>
              </>
            ) : (
              <Button
                onClick={() => {
                  login();
                  setIsMenuOpen(false);
                }}
                className="flex items-center justify-center gap-2 w-full"
              >
                <LogIn size={16} />
                Sign In
              </Button>
            )}
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
