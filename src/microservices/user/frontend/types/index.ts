
export interface User {
  id: string;
  name: string;
  email: string;
  phone?: string;
  profilePicture?: string;
  address?: string;
  city?: string;
  state?: string;
  zipCode?: string;
  driverLicense?: string;
  isVerified?: boolean;
}
