
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from "sonner";
import { User } from '../types';

interface AuthContextType {
  isAuthenticated: boolean;
  user: User | null;
  login: () => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType>({
  isAuthenticated: false,
  user: null,
  login: () => {},
  logout: () => {}
});

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState<User | null>(null);
  const navigate = useNavigate();
  
  // In a real application, this would be replaced with Auth0 SDK code
  useEffect(() => {
    // Check for existing auth state in localStorage (this is a mock)
    const savedAuth = localStorage.getItem('auth');
    if (savedAuth) {
      try {
        const authData = JSON.parse(savedAuth);
        setIsAuthenticated(true);
        setUser(authData.user);
      } catch (error) {
        console.error("Failed to parse auth data", error);
        localStorage.removeItem('auth');
      }
    }
  }, []);
  
  const login = () => {
    // Mock login - in reality this would trigger Auth0 login flow
    const mockUser = {
      id: "user_123",
      name: "John Doe",
      email: "john.doe@example.com"
    };
    
    setUser(mockUser);
    setIsAuthenticated(true);
    localStorage.setItem('auth', JSON.stringify({ user: mockUser }));
    toast.success("Successfully signed in!");
    navigate('/dashboard');
  };
  
  const logout = () => {
    setIsAuthenticated(false);
    setUser(null);
    localStorage.removeItem('auth');
    toast.info("You have been signed out");
    navigate('/');
  };
  
  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
